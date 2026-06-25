

# ===============================================================================
# Copyright 2021 An-Jun Liu
# Modifiy 2026 Lin Pai-Shao
# Last Modifd Date: 06/25/2026
# ===============================================================================

import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from math import pi
import matplotlib.patches as patches
from scipy.stats import norm
import seaborn as sns; sns.set()
from datetime import date
DEBUG = 1

# Utilities function
def ratioSigma(mu_y, sigma_y, mu_x, sigma_x,ratio):
    return np.sqrt((sigma_y/mu_y)**2 + (sigma_x/mu_x)**2)*ratio

def minusSigma(sigma_x, sigma_y):
    return np.sqrt(sigma_x**2 + sigma_y**2)

# T0 regression fitting functions
# ===============================================================================
def linear(x, a, b):
    return a*x + b

def average(x, a):
    return 0*x + a

fit_func_list = [linear, average]

# functions for button
# ===============================================================================
def calculateT0(fit_function_type, v_t, mask,num):
    """
    Input:
    1. fit_function_type: 0 for linear, 1 for average

    2. v_t: raw voltage-time data

    3. mask: table of selected points

    Output:
    return [status, T0, T0_SIGMA, R^2]

    status: 
    0 success

    1 failed at fitting data from which the outliers are removed
    
    """

    # initialization
    T0 = np.zeros(5)
    T0_SIGMA = np.zeros(5)
    R = np.zeros(5)
    
    r = 0
    status = 0
    fig, axs= plt.subplots(2, 3, figsize = (16,8))
    f = fit_func_list[fit_function_type]

    # go over Ar 36 to 40
    for i in range(5):
        # first linear regression 
        # fit whole raw data (no outlier is removed)
        n=0
        t = v_t[i, :, 1]
        v = v_t[i, :, 0]
        popt, _ = curve_fit(f, t, v)
        T0[i] = f(0, *popt)
        T0_SIGMA[i] = (np.std(np.abs(v - f(t, *popt))))/(np.sqrt(num))  # std of the error
        
        axs[i//3, i%3].plot(t, v, marker = 'o', label = "raw data")
        axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line")
        R[i] = r2_score(v,f(t, *popt))
        axs[i//3, i%3].set(xlabel = "t (sec)", ylabel = "mV")
        error = T0_SIGMA[i]
        # second linear regression 
        # remove the manually selected outliers if necessary
        if  (R[i] <= 0.8):
            x = 0
            for j in range(num-1):
                r = v[j-x]-f(t[j-x], *popt)
                if r < 0 :
                    r = r *-1
                if r > error and x < 4:
                    x = x+1
                    mask[i, j] = 0
                    n=n+1
                if (mask[i, :] == 0).any():
                    selected_indices = np.where(mask[i, :] == 1)[0]
                    removed_indices = np.where(mask[i, :] == 0)[0]
                
                    t = v_t[i, selected_indices, 1]
                    v = v_t[i, selected_indices, 0]
                    
                    try:
                        popt, _ = curve_fit(f, t, v)
                        T0[i] = f(0, *popt)
                        T0_SIGMA[i] = (np.std(np.abs(v - f(t, *popt))))/(np.sqrt((num-n)))  # std of the error of second fit
                        R[i] = r2_score(v,f(t, *popt))
                    except:
                        status = 1
                    axs[i//3, i%3].plot(v_t[i, removed_indices, 1], v_t[i, removed_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                    axs[i//3, i%3].ticklabel_format(axis='y', style='sci', scilimits=(0,0))          
            axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line\n(exclude outliers)")
            
        axs[i//3, i%3].legend(bbox_to_anchor=(0.7,1.2), loc='upper left')
        axs[i//3, i%3].set_title("Ar {}\n{} = {} \nerror = {}\nR^2 = {}".format(i+36, r'$T_{0}$', '{:0.5e}'.format(T0[i]), '{:0.5e}'.format(T0_SIGMA[i]),'{:0.5e}'.format(R[i])), loc='left')
    
    axs[1,2].axis('off')
    plt.tight_layout()
    plt.savefig(".work/LR.png", dpi=200)
    plt.clf()
    plt.close("all")

    return [status, T0, T0_SIGMA, R],mask

def REcalculateT0(fit_function_type, v_t, mask,num):
    """
    Input:
    1. fit_function_type: 0 for linear, 1 for average

    2. v_t: raw voltage-time data

    3. mask: table of selected points

    Output:
    return [status, T0, T0_SIGMA, R^2]

    status: 
    0 success

    1 failed at fitting data from which the outliers are removed
    
    """

    # initialization
    T0 = np.zeros(5)
    T0_SIGMA = np.zeros(5)
    R = np.zeros(5)
    
    status = 0
    fig, axs = plt.subplots(2, 3, figsize = (16,8))
    f = fit_func_list[fit_function_type]

    # go over Ar 36 to 40
    for i in range(5):
        # first linear regression 
        # fit whole raw data (no outlier is removed)
        n=0
        t = v_t[i, :, 1]
        v = v_t[i, :, 0]
        popt, _ = curve_fit(f, t, v)
        T0[i] = f(0, *popt)
        for j in range(num):
            if mask[i,j]==0:
                n=n+1
        T0_SIGMA[i] = (np.std(np.abs(v - f(t, *popt))))/(np.sqrt((num-n)))  # std of the error
        
        axs[i//3, i%3].plot(t, v, marker = 'o', label = "raw data")
        axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line")
        R[i] = r2_score(v,f(t, *popt))
        axs[i//3, i%3].set(xlabel = "t (sec)", ylabel = "mV")

        # second linear regression 
        # remove the manually selected outliers if necessary
        if (mask[i, :] == 0).any():
            selected_indices = np.where(mask[i, :] == 1)[0]
            removed_indices = np.where(mask[i, :] == 0)[0]
            
            t = v_t[i, selected_indices, 1]
            v = v_t[i, selected_indices, 0]
            
            try:
                popt, _ = curve_fit(f, t, v)
                T0[i] = f(0, *popt)
                T0_SIGMA[i] = (np.std(np.abs(v - f(t, *popt))))/(np.sqrt((num-n))) # std of the error of second fit
                axs[i//3, i%3].plot(t, f(t, *popt), linestyle = '--', label = "fitted line\n(exclude outliers)")
                R[i] = r2_score(v,f(t, *popt))
            except:
                status = 1
                
            axs[i//3, i%3].plot(v_t[i, removed_indices, 1], v_t[i, removed_indices, 0], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
            axs[i//3, i%3].ticklabel_format(axis='y', style='sci', scilimits=(0,0))
       
        axs[i//3, i%3].legend(bbox_to_anchor=(0.7,1.2), loc='upper left')
        axs[i//3, i%3].set_title("Ar {}\n{} = {} \nerror = {}\nR^2 = {}".format(i+36, r'$T_{0}$', '{:0.5e}'.format(T0[i]), '{:0.5e}'.format(T0_SIGMA[i]),'{:0.5e}'.format(R[i])), loc='left')
    
    axs[1,2].axis('off')
    plt.tight_layout()
    plt.savefig(".work/LR.png", dpi=200)
    plt.clf()
    plt.close("all")

    return [status, T0, T0_SIGMA, R]

def getDFStatistics_ls(file, mask,constants, Ncolor, Nmaker):
    fig, n = plt.subplots()
    with open(file, 'r') as f:
        data = f.readlines()
            
    # check header here
    if data[0].rstrip() != "Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle":
        raise Exception("Wrong data format!")
    
    i = 0
    while i != (len(data)-2):
        if data[i].split(',')[17] == "nan":
            data.pop(i)
            i=i-1
        i=i+1

    x = np.zeros(len(data)-2)  
    y = np.zeros(len(x)) 
    x_std = np.zeros(len(x)) 
    y_std = np.zeros(len(x)) 
    T_all = np.zeros(len(x)) 
    T_std_all = np.zeros(len(x)) 
    T_sum = 0 
    mswd = 0
    wma = 0
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[46])/float(data[i+1].split(',')[7]) 
        y[i] = float(data[i+1].split(',')[61])/float(data[i+1].split(',')[7])
        x_std[i] = float(data[i+1].split(',')[47])/float(data[i+1].split(',')[8]) 
        y_std[i] = float(data[i+1].split(',')[62])/float(data[i+1].split(',')[8])
        T_all[i] = float(data[i+1].split(',')[17])
        T_std_all[i] = float(data[i+1].split(',')[18])
    j = 0
    for i in range (len(y)):
        if x[i-j] < 0 or y[i-j] < 0:
            x = np.delete(x,[i-j])
            y = np.delete(y,[i-j])
            x_std = np.delete(x_std,[i-j])
            y_std = np.delete(y_std,[i-j])
            T_all = np.delete(T_all,[i-j])
            T_std_all = np.delete(T_std_all,[i-j])
            j = j+1
            
    popt, _ = curve_fit(linear, x, y)
    n.plot(x,y,marker = Nmaker,linestyle = 'None', label = "data")
    n.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line")
    n.set_xlabel('39^Ar/36^Ar')
    n.set_ylabel('40^Ar/36^Ar')
   
    if (mask[:] == 0).any():
        j = 0
        for i in range(len(y)):
            if(mask[i]==0):
                fx = x[i-j]
                fy = y[i-j]
                x = np.delete(x,[i-j])
                y = np.delete(y,[i-j])
                x_std = np.delete(x_std,[i-j])
                y_std = np.delete(y_std,[i-j])
                T_all = np.delete(T_all,[i-j])
                T_std_all = np.delete(T_std_all,[i-j])
                n.plot(fx, fy, marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
    for i in range (len(y)): 
        t = np.linspace(0, 2*pi, 100)
        n.plot( x[i]+x_std[i]*np.cos(t) , y[i]+y_std[i]*np.sin(t),color='lightgray',linestyle='-')
    popt, _ = curve_fit(linear, x, y)
    n.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line(exclude outliers)", color = Ncolor)
    
    popt, _ = curve_fit(linear, x, y)
    n.plot(0, linear(0, *popt), marker = Nmaker,linestyle = 'None', label = "fitted line(exclude outliers)", color = 'r')
    n = linear(0,*popt)
    popt, _ = curve_fit(linear, x_std, y_std)
    n_std = linear(0,*popt)    
    
    plt.savefig(".work/DFN.png", dpi = 200)
    
    fig, iv = plt.subplots()
    
    x = np.zeros(len(data)-2)  
    y = np.zeros(len(x)) 
    x_std = np.zeros(len(x)) 
    y_std = np.zeros(len(x)) 
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[46])/float(data[i+1].split(',')[61]) 
        y[i] = float(data[i+1].split(',')[7])/float(data[i+1].split(',')[61])
        x_std[i] = float(data[i+1].split(',')[47])/float(data[i+1].split(',')[62]) 
        y_std[i] = float(data[i+1].split(',')[8])/float(data[i+1].split(',')[62])
     
    j = 0
    for i in range (len(y)):
        if x[i-j] < 0 or y[i-j] < 0:
            x = np.delete(x,[i-j])
            y = np.delete(y,[i-j])
            x_std = np.delete(x_std,[i-j])
            y_std = np.delete(y_std,[i-j])
            j = j+1
    
    popt, _ = curve_fit(linear, x, y)
    iv.plot(x,y,marker = Nmaker,linestyle = 'None', label = "data")
    iv.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line")
    iv.set_xlabel('39^Ar/40^Ar')
    iv.set_ylabel('36^Ar/40^Ar')
   
    if (mask[:] == 0).any():
        j = 0
        for i in range(len(y)):
            if(mask[i]==0):
                fx = x[i-j]
                fy = y[i-j]
                x = np.delete(x,[i-j])
                y = np.delete(y,[i-j])
                x_std = np.delete(x_std,[i-j])
                y_std = np.delete(y_std,[i-j])
                iv.plot(fx, fy, marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
    for i in range (len(y)): 
        t = np.linspace(0, 2*pi, 100)
        iv.plot( x[i]+x_std[i]*np.cos(t) , y[i]+y_std[i]*np.sin(t),color='lightgray',linestyle='-')
      
    iv.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line(exclude outliers)",color = Ncolor)
    
    popt, _ = curve_fit(linear, x, y,)
    a = -popt[1]/popt[0]
    iv.plot(a,0,  marker = Nmaker,linestyle = 'None', label = "fitted line(exclude outliers)", color = 'r')
    iv = linear(0,*popt)
    popt, _ = curve_fit(linear, x_std, y_std)
    iv_std = linear(0,*popt)    
    
    plt.savefig(".work/DFI.png", dpi = 200)
    
    J = float(data[1].split(',')[4])
    J_std = float(data[1].split(',')[5])
    T = np.log(1 + J*iv) / float(constants[14])
    T_std = np.sqrt((J**2 * iv_std**2 + iv**2 * J_std**2)/ ((float(constants[14])*(1+iv*J))**2))
    
    for i in range(len(y)):
        T_sum = T_sum + T_all[i]
    T_sum = T_sum/len(y)

    for i in range(len(y)):
        mswd = (((T_sum-T_all[i])**2)/(T_std_all[i]**2))+mswd
    mswd = 1/(len(y)-1)*mswd

    for i in range(len(y)):
        wma = wma+((1/(T_std_all[i]**2)*T_all[i])/(1/(T_std_all[i]**2)))
    plt.clf()
    plt.close("all")

    return [n,n_std,iv,iv_std,mswd,wma,T,T_std]

def getDFStatistics_sh(file, mask,constants,Ncolor, Nmaker):
    fig, n = plt.subplots()
    with open(file, 'r') as f:
        data = f.readlines()
            
    # check header here
    if data[0].rstrip() != "Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle":
        raise Exception("Wrong data format!")
    
    i = 0
    while i != (len(data)-2):
        if data[i].split(',')[17] == "nan":
            data.pop(i)
            i=i-1
        i=i+1

    x = np.zeros(len(data)-2)  
    y = np.zeros(len(x)) 
    x_std = np.zeros(len(x)) 
    y_std = np.zeros(len(x)) 
    T_all = np.zeros(len(x)) 
    T_std_all = np.zeros(len(x)) 
    T_sum = 0 
    mswd = 0
    wma = 0
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[46])/float(data[i+1].split(',')[7]) 
        y[i] = float(data[i+1].split(',')[61])/float(data[i+1].split(',')[7])
        x_std[i] = float(data[i+1].split(',')[47])/float(data[i+1].split(',')[8]) 
        y_std[i] = float(data[i+1].split(',')[62])/float(data[i+1].split(',')[8])
        T_all[i] = float(data[i+1].split(',')[17])
        T_std_all[i] = float(data[i+1].split(',')[18])
    
    popt, _ = curve_fit(linear, x, y)
    n.plot(x,y,marker = 'o',linestyle = 'None', label = "data")
    n.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line")
    n.set_xlabel('39^Ar/36^Ar')
    n.set_ylabel('40^Ar/36^Ar')
   
    if (mask[:] == 0).any():
        j = 0
        for i in range(len(y)):
            if(mask[i]==0):
                fx = x[i-j]
                fy = y[i-j]
                x = np.delete(x,[i-j])
                y = np.delete(y,[i-j])
                x_std = np.delete(x_std,[i-j])
                y_std = np.delete(y_std,[i-j])
                T_all = np.delete(T_all,[i-j])
                T_std_all = np.delete(T_std_all,[i-j])
                n.plot(fx, fy, marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
    for i in range (len(y)): 
        t = np.linspace(0, 2*pi, 100)
        n.plot( x[i]+x_std[i]*np.cos(t) , y[i]+y_std[i]*np.sin(t),color='lightgray',linestyle='-')
    popt, _ = curve_fit(linear, x, y)
    n.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line(exclude outliers)", color = Ncolor)
    
    popt, _ = curve_fit(linear, x, y)
    n.plot(0, linear(0, *popt), marker = Nmaker,linestyle = 'None', label = "fitted line(exclude outliers)", color = 'r')
    n = linear(0,*popt)
    popt, _ = curve_fit(linear, x_std, y_std)
    n_std = linear(0,*popt)    
    
    plt.savefig(".work/DFN.png", dpi = 200)
    
    fig, iv = plt.subplots()
    
    x = np.zeros(len(data)-2)  
    y = np.zeros(len(x)) 
    x_std = np.zeros(len(x)) 
    y_std = np.zeros(len(x)) 
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[46])/float(data[i+1].split(',')[61]) 
        y[i] = float(data[i+1].split(',')[7])/float(data[i+1].split(',')[61])
        x_std[i] = float(data[i+1].split(',')[47])/float(data[i+1].split(',')[62]) 
        y_std[i] = float(data[i+1].split(',')[8])/float(data[i+1].split(',')[62])
     
    popt, _ = curve_fit(linear, x, y)
    iv.plot(x,y,marker = Nmaker,linestyle = 'None', label = "data")
    iv.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line")
    iv.set_xlabel('39^Ar/40^Ar')
    iv.set_ylabel('36^Ar/40^Ar')
   
    if (mask[:] == 0).any():
        j = 0
        for i in range(len(y)):
            if(mask[i]==0):
                fx = x[i-j]
                fy = y[i-j]
                x = np.delete(x,[i-j])
                y = np.delete(y,[i-j])
                x_std = np.delete(x_std,[i-j])
                y_std = np.delete(y_std,[i-j])
                iv.plot(fx, fy, marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
    for i in range (len(y)): 
        t = np.linspace(0, 2*pi, 100)
        iv.plot( x[i]+x_std[i]*np.cos(t) , y[i]+y_std[i]*np.sin(t),color='lightgray',linestyle='-')
      
    iv.plot(x, linear(x, *popt), linestyle = '--', label = "fitted line(exclude outliers)",color = Ncolor)
    
    popt, _ = curve_fit(linear, x, y,)
    a = -popt[1]/popt[0]
    iv.plot(a,0,  marker = Nmaker,linestyle = 'None', label = "fitted line(exclude outliers)", color = 'r')
    iv = linear(0,*popt)
    popt, _ = curve_fit(linear, x_std, y_std)
    iv_std = linear(0,*popt)    
    
    plt.savefig(".work/DFI.png", dpi = 200)
    
    J = float(data[1].split(',')[4])
    J_std = float(data[1].split(',')[5])
    T = np.log(1 + J*iv) / float(constants[14])
    T_std = np.sqrt((J**2 * iv_std**2 + iv**2 * J_std**2)/ ((float(constants[14])*(1+iv*J))**2))
    
    for i in range(len(y)):
        T_sum = T_sum + T_all[i]
    T_sum = T_sum/len(y)

    for i in range(len(y)):
        mswd = (((T_sum-T_all[i])**2)/(T_std_all[i]**2))+mswd
    mswd = 1/(len(y)-1)*mswd

    for i in range(len(y)):
        wma = wma+((1/(T_std_all[i]**2)*T_all[i])/(1/(T_std_all[i]**2)))
        
    plt.clf()
    plt.close("all")

    return [n,n_std,iv,iv_std,mswd,wma,T,T_std]

def getSHStatistics(file, mask,constants):
    fig, w = plt.subplots()
    with open(file, 'r') as f:
        data = f.readlines()
            
    # check header here
    if data[0].rstrip() != "Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle":
        raise Exception("Wrong data format!")
    
    i = 0
    while i != (len(data)-2):
        if data[i].split(',')[17] == "nan":
            data.pop(i)
            i=i-1
        i=i+1

    x = np.zeros(len(data)-2)  
    y = np.zeros(len(x)) 
    y_std = np.zeros(len(x)) 
    avg = 0
    mx = 0
    sum39 = 0
    sum40 = 0
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[22])
        y[i] = float(data[i+1].split(',')[17])/1000000
        y_std[i] = float(data[i+1].split(',')[18])/1000000
        sum39 = float(data[i+1].split(',')[13]) + sum39
        sum40 = float(data[i+1].split(',')[15]) + sum40
        avg = y[i]+avg
        if mx < y[i]:
            mx = y[i]
    avg = avg/len(x)
    
    j = 0
    for i in range(len(x)):        
        if i == 0:
            square = patches.Rectangle((0, y[i]-y_std[i]), x[i], y_std[i]*2, edgecolor='purple', facecolor='purple')
        else:
            square = patches.Rectangle((j, y[i]-y_std[i]), x[i], y_std[i]*2, edgecolor='purple', facecolor='purple')
        w.add_patch(square)
        j = x[i]+j
    
    plt.xlim(0, 100)
    plt.ylim(-10, mx+10)
    
    if (mask[:] == 0).any():
        avg = 0
        j = 0
        f = 0
        for i in range(len(y)):
            if(mask[i]==0):
                if i == 0:
                    fx = x[i-j]/2
                else:
                    f = x[0]
                    for k in range(i-1):
                        f = x[k+1-j]+f    
                    fx = x[i-j]/2+f
                fy = y[i-j]
                sum39 = sum39 - float(data[i+1].split(',')[13]) 
                sum40 = sum40 - float(data[i+1].split(',')[15])
                x = np.delete(x,[i-j])
                y = np.delete(y,[i-j])
                y_std = np.delete(y_std,[i-j])
                w.plot(fx, fy, marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
        for i in range(len(x)):
            avg = y[i]+avg
        avg = avg/len(x)
  
    w.plot((0,100), (avg,avg), linestyle = '-', label = "fitted line")
    w.set_xlabel('Cumulative 39^Ar Released(%)')
    w.set_ylabel('Age(Ma)')  
  
    plt.savefig(".work/DFW.png", dpi = 200)
    w = avg
    
    fig, a = plt.subplots()
    
    i = 0
    while i != (len(data)-2):
        if data[i].split(',')[17] == "nan":
            data.pop(i)
            i=i-1
        i=i+1

    x = np.zeros(len(data)-2)  
    y = np.zeros(len(x)) 
    y_std = np.zeros(len(x)) 
    avg = 0
    mx = 0
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[22])
        y[i] = float(data[i+1].split(',')[23])
        y_std[i] = float(data[i+1].split(',')[24])
        avg = y[i]+avg
        if mx < y[i]:
            mx = y[i]
    avg = avg/len(x)
    j = 0
    
    for i in range(len(x)):        
        if i == 0:
            square = patches.Rectangle((0, y[i]-y_std[i]), x[i], y_std[i]*2, edgecolor='purple', facecolor='purple')
        else:
            square = patches.Rectangle((j, y[i]-y_std[i]), x[i], y_std[i]*2, edgecolor='purple', facecolor='purple')
        a.add_patch(square)
        j = x[i]+j
    
    plt.xlim(0, 100)
    plt.ylim(-10, mx+10)
    
    if (mask[:] == 0).any():
        avg = 0
        j = 0
        f = 0
        for i in range(len(y)):
            if(mask[i]==0):
                if i == 0:
                    fx = x[i-j]/2
                else:
                    f = x[0]
                    for k in range(i-1):
                        f = x[k+1-j]+f    
                    fx = x[i-j]/2+f
                fy = y[i-j]
                x = np.delete(x,[i-j])
                y = np.delete(y,[i-j])
                y_std = np.delete(y_std,[i-j])
                a.plot(fx, fy, marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
        
        for i in range(len(x)):
            avg = y[i]+avg
        avg = avg/len(x)
  
    a.plot((0,100), (avg,avg), linestyle = '-', label = "fitted line")
    a.set_xlabel('Cumulative 39^Ar Released(%)')
    a.set_ylabel('K/Ca')  
  
    plt.savefig(".work/DFA.png", dpi = 200)

    F = sum40/sum39
    T = np.log(1 + float(data[1].split(',')[4])*F) / float(constants[14])
    
    plt.clf()
    plt.close("all")
    return [w,T]


def getDFStatistics_t(file, mask,power):
    fig, ax = plt.subplots()
    with open(file, 'r') as f:
        data = f.readlines()
            
    # check header here
    if data[0].rstrip() != "Samp#,Min,IRR,deg C,J,J_std,J_int,36Ar(a),36Ar(a)_std,37Ar(ca),37Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,40Ar(r),40Ar(r)_std,Age(Ma),Age_std(Ma),40Ar(r)(%),39Ar(k)(%),40Ar(r)(%)(step heating),39Ar(k)(%)(step heating),K/Ca,K/Ca_std,Degassing Patterns,36Ar(a),36Ar(a)_std,36Ar(c),36Ar(c)_std,36Ar(ca),36Ar(ca)_std,36Ar(cl),36Ar(cl)_std,37Ar(ca),37Ar(ca)_std,38Ar(a),38Ar(a)_std,38Ar(c),38Ar(c)_std,38Ar(k),38Ar(k)_std,38Ar(ca),38Ar(ca)_std,38Ar(cl),38Ar(cl)_std,39Ar(k),39Ar(k)_std,39Ar(ca),39Ar(ca)_std,40Ar(r),40Ar(r)_std,40Ar(a),40Ar(a)_std,40Ar(c),40Ar(c)_std,40Ar(k),40Ar(k)_std,Additional Parameters,40(r)/39(k),40(r)/39(k)_std,40(r+a),40(r+a)_std,40Ar/39Ar,40Ar/39Ar_std,37Ar/39Ar,37Ar/39Ar_std,36Ar/39Ar,36Ar/39Ar_std,Parameters,39Ar/37Ar(ca),39Ar/37Ar(ca)_std,36Ar/37Ar(ca),36Ar/37Ar(ca)_std,40Ar/39Ar(k),40Ar/39Ar(k)_std,38Ar/39Ar(k),38Ar/39Ar(k)_std,36Ar/38Ar(cl),36Ar/38Ar(cl)_std,40Ar/36Ar(a),40Ar/36Ar(a)_std,38Ar/36Ar(a),38Ar/36Ar(a)_std,?,numCycle":
        raise Exception("Wrong data format!")
    
    j = 0
    for i in range (len(data)-2):
        if float(data[i+1-j].split(',')[46])/float(data[i+1-j].split(',')[7]) < 0 or float(data[i+1-j].split(',')[61])/float(data[i+1-j].split(',')[7]) < 0 :
            data.pop(i-j)
            j=j+1  
        if data[i+1-j].split(',')[17] == "nan":
            data.pop(i-j)
            j=j+1

    x = np.zeros(len(data)-2)
    
    for i in range (len(data)-2):
        x[i] = float(data[i+1].split(',')[17])/pow(10,int(power))
   
    if (mask[:] == 0).any():
        j = 0
        for i in range(len(x)):
            if(mask[i]==0):
                x = np.delete(x,[i-j])
                j=j+1
    
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    
    fig, ax = plt.subplots()
    bins = np.arange(-5, x[len(x)-1]+5)
    
    for count, edge in zip(*np.histogram(x, bins)):
        for i in range(count):
            ax.add_patch(plt.Rectangle((edge, i), 1, 1,
                                       alpha=0.5))
    
    x_d = np.linspace(-x[0]-5, x[len(x)-1]+5, 2000)
        
    density = sum(norm(xi).pdf(x_d) for xi in x)

    plt.fill_between(x_d, density, alpha=0.5, color = 'r')
    plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth=1)
    
    plt.axis([x[0]-5, x[len(x)-1]+5, -0.2, len(x)])

    ax.set_xlabel('Age(10^'+str(power)+')')
    
    plt.savefig(".work/DFK.png", dpi = 200)
    plt.clf()
    plt.close("all")
    
    return 0

def getAirRatioStatistics(filelist):
    '''
    background1: published Ar 40/36 air background
    background2: published Ar 38/36 air background
    '''
    ratios = np.zeros((len(filelist), 2)) # [ratio pair, ratio value]

    for i, filename in enumerate(filelist):
        with open(filename, 'r') as f:
            data = f.readlines()

        # check header here
        if data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma":
            raise Exception("Wrong data format!")

        ratios[i, 0] = float(data[4].split(',')[9])
        ratios[i, 1] = float(data[5].split(',')[9])
        
    for i in range(len(ratios)):
        if abs(ratios[i,0]) > 313 :
            ratios = np.delete(ratios,i,0)

    n = len(ratios)

    # calculate statistics
    statistics = np.zeros((2, 2)) # [ratio pair, mean/std]
    for i in range(2):
        statistics[i, 0] = np.mean(ratios[:, i])
        statistics[i, 1] = np.std(ratios[:, i])

    # plot air ratio distribution
    fig, axs = plt.subplots(1, 2, figsize = (6,4))
    ratio_pair = ["Ar 40/36", "Ar 38/36"]
    for i in range(2):
        axs[i].plot(np.zeros(len(filelist)), ratios[:, i], marker = 'x', markersize = 10, linestyle = 'None')
        axs[i].errorbar(0, statistics[i, 0], yerr = statistics[i, 1], color = 'k', capthick = 2, capsize = 3, marker = '_', markersize = 15)
        axs[i].set_aspect(7/axs[i].get_data_ratio())
        axs[i].axes.get_xaxis().set_visible(False)  # remove the x-axis and its ticks
        axs[i].set_title(ratio_pair[i])

    #plt.show()
    plt.savefig(".work/ARS.png", dpi = 200)

    return statistics,n

def getJStatistics(file, mask):
    plt.figure().clear()
    result = np.zeros(len(file))
    std = np.zeros(len(file))
    fx = np.zeros(len(file))
    avg_y = np.zeros(len(file))
    stdp = np.zeros(len(file))
    stdn = np.zeros(len(file))
    mean_y = np.zeros(len(file))
    meanp = np.zeros(len(file))
    meann = np.zeros(len(file))
    avg = 0.0
    mean = 0.0
    mean_std = 0.0
    
    for i, filename in enumerate(file):
        with open(filename, 'r') as f:
            data = f.readlines()
            
        # check header here
        if data[0].rstrip() != "file name,36Ar(a)[V],37Ar(ca)[V],39Ar(k)[V],40Ar(r)[V],40Ar(r)(%),39Ar(k)(%),K/Ca,K/Ca Sigma,J value,J Sigma,J Sigma int":
            raise Exception("Wrong data format!")

      
        result[i] = float(data[1].split(',')[9])
        std[i] = float(data[1].split(',')[10])
        mean = mean + (1/(std[i]**2)*result[i])
        mean_std = mean_std + 1/(std[i]**2)
        avg = avg + float(data[1].split(',')[9])
        fx[i] = i+1
    y = result
    y_std = std
    x = fx
    avg = avg/len(file)
    mean = mean/mean_std
    mean_std = np.sqrt(1/mean_std)
    y_stdp = (np.std(y)/len(y)**0.5) + avg
    y_stdn = avg - (np.std(y)/len(y)**0.5)
    
    for i in range (len(y)):
        if y[i] < y_stdn:
            mask[i] = 0
        if y[i] > y_stdp:
            mask[i] = 0
        
    for i in range (len(y)):
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
    for i, filename in enumerate(file):
        avg_y[i] = avg
    plt.plot(x,y,marker = 'o', label = "J data")
    plt.plot(x,avg_y,linestyle = '-', label = "average") 
    plt.plot(x,stdp,linestyle = '--', label = "std+") 
    plt.plot(x,stdn,linestyle = '--', label = "std-") 
        
           
    if (mask[:] == 0).any():
        avg = 0.0
        j = 0
        for i, filename in enumerate(file):
            if(mask[i]==0 and len(y)>1):
                x = np.delete(x,[i-j])
                np.where(x<i,x,x-1)
                y = np.delete(y,[i-j])
                y_std = np.delete(y_std,[i-j])
                plt.plot(fx[i], result[i], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
        avg_y = np.zeros(len(y))
        for i in range (len(y)): 
            avg = avg+y[i]
            mean = mean + (1/(y_std[i]**2)*y[i])
            mean_std = mean_std + 1/(y_std[i]**2)
        avg = avg/len(y) 
        mean = mean/mean_std
        mean_std = np.sqrt(1/mean_std)
        y_stdp = np.std(y) + avg
        y_stdn = avg-np.std(y)
        stdp = np.zeros(len(y))
        stdn = np.zeros(len(y))
        for i in range (len(y)):
            avg_y[i] = avg
            mean_y[i] = mean
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
            
           
        plt.plot(x, avg_y, linestyle = '-', label = "average\n(exclude outliers)")
        plt.plot(x,stdp,linestyle = '--', label = "std+") 
        plt.plot(x,stdn,linestyle = '--', label = "std-") 
           
    #plt.show()
    plt.savefig(".work/J.png", dpi = 200)
    plt.clf()
    plt.close("all")

    return [avg,(y_stdp-avg),mean,mean_std],mask

def getSaltStatistics(file, mask,salt):
    plt.figure().clear()
    result = np.zeros(len(file))
    std = np.zeros(len(file))
    fx = np.zeros(len(file))
    avg_y = np.zeros(len(file))
    stdp = np.zeros(len(file))
    stdn = np.zeros(len(file))
    mean_y = np.zeros(len(file))
    meanp = np.zeros(len(file))
    meann = np.zeros(len(file))
    avg = 0.0
    mean = 0.0
    mean_std = 0.0
    
    
    for i, filename in enumerate(file):
        with open(filename, 'r') as f:
            data = f.readlines()
            
        # check header here
        if data[0].rstrip() != "Samp#,,Ratio,Sigma":
            raise Exception("Wrong data format!")

        if(salt==39 or salt == 38):
            result[i] = float(data[2].split(',')[2])
            avg = avg + float(data[2].split(',')[2])
            std[i] = float(data[2].split(',')[3])
            mean = mean + (1/(std[i]**2)*result[i])
            mean_std = mean_std + 1/(std[i]**2)
            fx[i] = i+1
        elif(salt==37):
            result[i] = float(data[3].split(',')[2])
            avg = avg + float(data[3].split(',')[2])
            std[i] = float(data[3].split(',')[3])
            mean = mean + (1/(std[i]**2)*result[i])
            mean_std = mean_std + 1/(std[i]**2)
            fx[i] = i+1
        else:
            result[i] = float(data[1].split(',')[2])
            avg = avg + float(data[1].split(',')[2])
            std[i] = float(data[1].split(',')[3])
            mean = mean + (1/(std[i]**2)*result[i])
            mean_std = mean_std + 1/(std[i]**2)
            fx[i] = i+1
            
    y = result
    y_std = std
    x = fx
    avg = avg/len(file)
    mean = mean/mean_std
    mean_std = np.sqrt(1/mean_std)
    y_stdp = (np.std(y)/len(y)**0.5) + avg
    y_stdn = avg - (np.std(y)/len(y)**0.5)
    
    for i in range (len(y)):
        if y[i] < y_stdn:
            mask[i] = 0
        if y[i] > y_stdp:
            mask[i] = 0
        
    for i in range (len(y)):
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
    for i, filename in enumerate(file):
        avg_y[i] = avg
    plt.plot(x,y,marker = 'o', label = "J data")
    plt.plot(x,avg_y,linestyle = '-', label = "average") 
    plt.plot(x,stdp,linestyle = '--', label = "std+") 
    plt.plot(x,stdn,linestyle = '--', label = "std-") 
        
           
    if (mask[:] == 0).any():
        avg = 0.0
        j = 0
        for i, filename in enumerate(file):
            if(mask[i]==0 and len(y)>1):
                x = np.delete(x,[i-j])
                np.where(x<i,x,x-1)
                y = np.delete(y,[i-j])
                y_std = np.delete(y_std,[i-j])
                plt.plot(fx[i], result[i], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
        avg_y = np.zeros(len(y))
        for i in range (len(y)): 
            avg = avg+y[i]
            mean = mean + (1/(y_std[i]**2)*y[i])
            mean_std = mean_std + 1/(y_std[i]**2)
        avg = avg/len(y) 
        mean = mean/mean_std
        mean_std = np.sqrt(1/mean_std)
        y_stdp = np.std(y) + avg
        y_stdn = avg-np.std(y)
        stdp = np.zeros(len(y))
        stdn = np.zeros(len(y))
        for i in range (len(y)):
            avg_y[i] = avg
            mean_y[i] = mean
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
            
           
        plt.plot(x, avg_y, linestyle = '-', label = "average\n(exclude outliers)")
        plt.plot(x,stdp,linestyle = '--', label = "std+") 
        plt.plot(x,stdn,linestyle = '--', label = "std-") 
           
    #plt.show()
    plt.savefig(".work/Salt.png", dpi = 200)
    plt.clf()
    plt.close("all")

    return [avg,(y_stdp-avg),mean,mean_std],mask

def REgetSaltStatistics(file, mask,salt):
    plt.figure().clear()
    result = np.zeros(len(file))
    std = np.zeros(len(file))
    fx = np.zeros(len(file))
    avg_y = np.zeros(len(file))
    stdp = np.zeros(len(file))
    stdn = np.zeros(len(file))
    mean_y = np.zeros(len(file))
    meanp = np.zeros(len(file))
    meann = np.zeros(len(file))
    avg = 0.0
    mean = 0.0
    mean_std = 0.0
    
    
    for i, filename in enumerate(file):
        with open(filename, 'r') as f:
            data = f.readlines()
            
        # check header here
        if data[0].rstrip() != "Samp#,,Ratio,Sigma":
            raise Exception("Wrong data format!")

        if(salt==39 or salt == 38):
            result[i] = float(data[2].split(',')[2])
            avg = avg + float(data[2].split(',')[2])
            std[i] = float(data[2].split(',')[3])
            mean = mean + (1/(std[i]**2)*result[i])
            mean_std = mean_std + 1/(std[i]**2)
            fx[i] = i+1
        else:
            result[i] = float(data[1].split(',')[2])
            avg = avg + float(data[1].split(',')[2])
            std[i] = float(data[1].split(',')[3])
            mean = mean + (1/(std[i]**2)*result[i])
            mean_std = mean_std + 1/(std[i]**2)
            fx[i] = i+1
            
    y = result
    y_std = std
    x = fx
    avg = avg/len(file)
    mean = mean/mean_std
    mean_std = np.sqrt(1/mean_std)
    y_stdp = (np.std(y)/len(y)**0.5) + avg
    y_stdn = avg - (np.std(y)/len(y)**0.5)
        
    for i in range (len(y)):
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
            
    for i, filename in enumerate(file):
        avg_y[i] = avg
    plt.plot(x,y,marker = 'o', label = "J data")
    plt.plot(x,avg_y,linestyle = '-', label = "average") 
    plt.plot(x,stdp,linestyle = '--', label = "std+") 
    plt.plot(x,stdn,linestyle = '--', label = "std-") 
        
           
    if (mask[:] == 0).any():
        avg = 0.0
        j = 0
        for i, filename in enumerate(file):
            if(mask[i]==0):
                x = np.delete(x,[i-j])
                np.where(x<i,x,x-1)
                y = np.delete(y,[i-j])
                y_std = np.delete(y_std,[i-j])
                plt.plot(fx[i], result[i], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
        avg_y = np.zeros(len(y))
        for i in range (len(y)): 
            avg = avg+y[i]
            mean = mean + (1/(y_std[i]**2)*y[i])
            mean_std = mean_std + 1/(y_std[i]**2)
        avg = avg/len(y) 
        mean = mean/mean_std
        mean_std = np.sqrt(1/mean_std)
        y_stdp = np.std(y) + avg
        y_stdn = avg-np.std(y)
        stdp = np.zeros(len(y))
        stdn = np.zeros(len(y))
        for i in range (len(y)):
            avg_y[i] = avg
            mean_y[i] = mean
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
            
           
        plt.plot(x, avg_y, linestyle = '-', label = "average\n(exclude outliers)")
        plt.plot(x,stdp,linestyle = '--', label = "std+") 
        plt.plot(x,stdn,linestyle = '--', label = "std-") 
           
    #plt.show()
    plt.savefig(".work/Salt.png", dpi = 200)
    plt.clf()
    plt.close("all")
    

    return [avg,(y_stdp-avg),mean,mean_std]

def REgetJStatistics(file, mask):
    plt.figure().clear()
    result = np.zeros(len(file))
    std = np.zeros(len(file))
    fx = np.zeros(len(file))
    avg_y = np.zeros(len(file))
    stdp = np.zeros(len(file))
    stdn = np.zeros(len(file))
    mean_y = np.zeros(len(file))
    meanp = np.zeros(len(file))
    meann = np.zeros(len(file))
    avg = 0.0
    mean = 0.0
    mean_std = 0.0
    
    for i, filename in enumerate(file):
        with open(filename, 'r') as f:
            data = f.readlines()
            
        # check header here
        if data[0].rstrip() != "file name,36Ar(a)[V],37Ar(ca)[V],39Ar(k)[V],40Ar(r)[V],40Ar(r)(%),39Ar(k)(%),K/Ca,K/Ca Sigma,J value,J Sigma,J Sigma int":
            raise Exception("Wrong data format!")

      
        result[i] = float(data[1].split(',')[9])
        std[i] = float(data[1].split(',')[10])
        mean = mean + (1/(std[i]**2)*result[i])
        mean_std = mean_std + 1/(std[i]**2)
        avg = avg + float(data[1].split(',')[9])
        fx[i] = i+1
    y = result
    y_std = std
    x = fx
    avg = avg/len(file)
    mean = mean/mean_std
    mean_std = np.sqrt(1/mean_std)
    y_stdp = (np.std(y)/len(y)**0.5) + avg
    y_stdn = avg - (np.std(y)/len(y)**0.5)
    for i in range (len(y)):
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
    for i, filename in enumerate(file):
        avg_y[i] = avg
    plt.plot(x,y,marker = 'o', label = "J data")
    plt.plot(x,avg_y,linestyle = '-', label = "average") 
    plt.plot(x,stdp,linestyle = '--', label = "std+") 
    plt.plot(x,stdn,linestyle = '--', label = "std-") 
        
           
    if (mask[:] == 0).any():
        avg = 0.0
        j = 0
        for i, filename in enumerate(file):
            if(mask[i]==0):
                x = np.delete(x,[i-j])
                np.where(x<i,x,x-1)
                y = np.delete(y,[i-j])
                y_std = np.delete(y_std,[i-j])
                plt.plot(fx[i], result[i], marker = 'x', markersize = 12, linestyle = 'None', color = 'r')
                j=j+1
        avg_y = np.zeros(len(y))
        for i in range (len(y)): 
            avg = avg+y[i]
            mean = mean + (1/(y_std[i]**2)*y[i])
            mean_std = mean_std + 1/(y_std[i]**2)
        avg = avg/len(y) 
        mean = mean/mean_std
        mean_std = np.sqrt(1/mean_std)
        y_stdp = np.std(y) + avg
        y_stdn = avg-np.std(y)
        stdp = np.zeros(len(y))
        stdn = np.zeros(len(y))
        for i in range (len(y)):
            avg_y[i] = avg
            mean_y[i] = mean
            stdp[i] = y_stdp
            stdn[i] = y_stdn
            meanp[i] = mean_std + avg
            meann[i] = avg - mean_std
            
           
        plt.plot(x, avg_y, linestyle = '-', label = "average\n(exclude outliers)")
        plt.plot(x,stdp,linestyle = '--', label = "std+") 
        plt.plot(x,stdn,linestyle = '--', label = "std-") 
           
    #plt.show()
    plt.savefig(".work/J.png", dpi = 200)
    plt.clf()
    plt.close("all")

    return [avg,(y_stdp-avg),mean,mean_std]

def getT0Statistics(file, mask):
    result = np.zeros((len(file), 5))
    
    for i, filename in enumerate(file):
        with open(filename, 'r') as f:
            data = f.readlines()
            
        # check header here
        if data[0].rstrip() != "Samp#,Min,T,Date,iradiation PK 90%,Mass,T0,T0_SIGMA,R^2":
            raise Exception("Wrong data format!")

        for j in range(5):
            result[i, j] = float(data[j+1].split(',')[6])

    # calculate statistics
    statistics = np.zeros((5, 2))

    for i in range(5):
        statistics[i, 0] = np.mean(result[:, i])
        statistics[i, 1] = np.std(result[:, i])
        for j in range(len(result)):
            if abs(result[j,i] - statistics[i,0]) > (statistics[i,1]/2)+statistics[i,0] :
                mask[j] = 0

    k = 0
    for i in range(len(result)):
        if mask[i] == 0:
            result = np.delete(result,i-k,0)             
            k +=1

    restatistics = np.zeros((5, 2))

    for i in range(5):
        restatistics[i, 0] = np.mean(result[:, i])
        restatistics[i, 1] = np.std(result[:, i])
    
    n = len(result)
    
    # plot T0 distribution
    fig, axs = plt.subplots(1, 5, figsize = (12,4))
    for i in range(5):
        axs[i].plot(np.zeros(len(result)), result[:, i], marker = 'x', markersize = 10, linestyle = 'None')
        axs[i].errorbar(0, restatistics[i, 0], yerr = restatistics[i, 1], color = 'k', capthick = 2, capsize = 3, marker = '_', markersize = 15)
        axs[i].set_aspect(7/axs[i].get_data_ratio())
        axs[i].axes.get_xaxis().set_visible(False)  # remove the x-axis and its ticks
        axs[i].set_title("Ar {}".format(36+i))

    #plt.show()
    plt.savefig(".work/T0S.png", dpi = 200)
    plt.clf()
    plt.close("all")

    return restatistics,mask,statistics,n

def REgetT0Statistics(file, mask):
    result = np.zeros((len(file), 5))
    
    for i, filename in enumerate(file):
        with open(filename, 'r') as f:
            data = f.readlines()
            
        # check header here
        if data[0].rstrip() != "Samp#,Min,T,Date,iradiation PK 90%,Mass,T0,T0_SIGMA,R^2":
            raise Exception("Wrong data format!")

        for j in range(5):
            result[i, j] = float(data[j+1].split(',')[6])

    # calculate statistics
    k = 0
    for i in range(len(result)):
        if mask[i] == 0:
            result = np.delete(result,i-k,0)             
            k +=1
       
    n = len(result)
    statistics = np.zeros((5, 2))

    for i in range(5):
        statistics[i, 0] = np.mean(result[:, i])
        statistics[i, 1] = np.std(result[:, i])
    
    # plot T0 distribution
    fig, axs = plt.subplots(1, 5, figsize = (12,4))
    for i in range(5):
        axs[i].plot(np.zeros(len(result)), result[:, i], marker = 'x', markersize = 10, linestyle = 'None')
        axs[i].errorbar(0, statistics[i, 0], yerr = statistics[i, 1], color = 'k', capthick = 2, capsize = 3, marker = '_', markersize = 15)
        axs[i].set_aspect(7/axs[i].get_data_ratio())
        axs[i].axes.get_xaxis().set_visible(False)  # remove the x-axis and its ticks
        axs[i].set_title("Ar {}".format(36+i))

    #plt.show()
    plt.savefig(".work/T0S.png", dpi = 200)
    plt.clf()
    plt.close("all")

    return statistics,n

pair_indices = [[3, 4], [0, 4], [3, 0], [4, 0], [2, 0]]
#               39/40    36/40   39/36   40/36   38/36
def calculateMassRatio(mass_filename, background_filename, OGD):
    raw = np.zeros((5, 2))
    preline = np.zeros((5,2))

    with open(mass_filename, 'r') as f:
        data = f.readlines()
       
    # check header here
    if data[0].rstrip() != "Samp#,Min,T,Date,iradiation PK 90%,Mass,T0,T0_SIGMA,R^2":
        raise Exception("Wrong data format!")
       
    info = (data[1].split(','))[0]
    t = (data[1].split(','))[2]
    Min = (data[1].split(','))[1]
    PK = (data[1].split(','))[4]
    SPD = date.fromisoformat(data[1].split(',')[3].replace('/',''))
    OGD = date.fromisoformat(OGD)
    T = SPD-OGD
    T = int(T.days)
   
   
    for i in range(5):
        raw[i, 0] = float(data[i+1].split(',')[6]) # T0
        raw[i, 1] = float(data[i+1].split(',')[7]) # T0_SIGMA

    with open(background_filename, 'r') as f:
        data = f.readlines()

    # check header here
    if data[0].rstrip() != "Samp#,Min,T,Date,iradiation PK 90%,Mass,T0,T0_SIGMA,R^2":
        raise Exception("Wrong data format!")

    for i in range(5):
        preline[i, 0] = float(data[i+1].split(',')[6]) # T0
        preline[i, 1] = float(data[i+1].split(',')[7]) # T0_SIGMA

    measurement = raw[:, 0] - preline[:, 0] # 36 37 38 39 40 (Measurement)
    measurement_std = np.sqrt(raw[:, 1]**2 + preline[:, 1]**2)
    measurement[1] = measurement[1] * np.exp(0.0198*T)
    measurement[3] = measurement[3] * np.exp(0.0000071*T)
   
    ratio = np.zeros(5)
    ratio_std = np.zeros(5)
    for i in range(5):
        y, x = pair_indices[i][0], pair_indices[i][1]
        ratio[i] = measurement[y]/measurement[x]
        ratio_std[i] = ratio[i]*np.sqrt((measurement_std[y]/measurement[y])**2 + (measurement_std[x]/measurement[x])**2)

    return [raw[:, 0], measurement, measurement_std, ratio, ratio_std,info,t,Min,PK]

def calculateSlatCa(salt):
    ratio = np.zeros((2,2))

    with open(salt, 'r') as f:
        data = f.readlines()

    # check header here
    if data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma":
        raise Exception("Wrong data format!")

    Ar36 = float(data[1].split(',')[6])    
    Ar36_std = float(data[1].split(',')[7])
    Ar37 = float(data[2].split(',')[6])    
    Ar37_std = float(data[2].split(',')[7])
    Ar39 = float(data[4].split(',')[6])    
    Ar39_std = float(data[4].split(',')[7])
    air = float(data[5].split(',')[6])
    air_std = float(data[5].split(',')[7])
    
    ratio[0,0] = (Ar36-air/298.56)/Ar37
    ratio[0,1] = ratio[0,0]*np.sqrt(((Ar36_std + air_std/298.56)/(Ar36 - air/298.56))**2 + (Ar37_std/Ar37)**2)
    ratio[1,0] = Ar39/Ar37
    ratio[1,1] = ratio[1,0]*np.sqrt((Ar39_std/Ar39)**2 + (Ar37_std/Ar37)**2)
    info = (data[1].split(','))[0]
    
    return ratio,info

def calculateSlatK(salt):
    ratio = np.zeros((3,2))

    with open(salt, 'r') as f:
        data = f.readlines()

    # check header here
    if data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma":
        raise Exception("Wrong data format!")

    Ar36 = float(data[1].split(',')[6])    
    Ar36_std = float(data[1].split(',')[7])
    Ar40 = float(data[5].split(',')[6])    
    Ar40_std = float(data[5].split(',')[7])
    Ar39 = float(data[4].split(',')[6])    
    Ar39_std = float(data[4].split(',')[7])
    Ar38 = float(data[3].split(',')[6])
    Ar38_std = float(data[3].split(',')[7])
    Ar37 = float(data[2].split(',')[6])
    Ar37_std = float(data[2].split(',')[7])

    ratio[0,0] = (Ar40-Ar36*298.56)/Ar39
    ratio[0,1] = ratio[0,0]*np.sqrt(((Ar40_std + Ar36_std*298.56) / (Ar40 - Ar36*298.56))**2 + (Ar39_std/Ar39)**2)
    ratio[1,0] = Ar38/Ar39
    ratio[1,1] = ratio[1,0]*np.sqrt((Ar38_std/Ar38)**2 + (Ar39_std/Ar39)**2)
    ratio[2,0] = Ar39/Ar37
    ratio[2,1] = ratio[2,0]*np.sqrt((Ar39_std/Ar39)**2 + (Ar37_std/Ar37)**2)
    info = (data[1].split(','))[0]

    return ratio,info

def getJVolumeStatistics(file, t,t_std,constants):
    l = 5.531*0.0000000001
    l_std = 0.0135*0.0000000001
    # collect data
    data = np.zeros((5, 2))

    with open(file,'r') as f:
        tmp_data = f.readlines()
    
    # check header here
    if tmp_data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma":
        raise Exception("Wrong data format!")

    for i in range(5):
        data[i, 0] = float(tmp_data[i+1].split(',')[6])
        data[i, 1] = float(tmp_data[i+1].split(',')[7])
    # Ar component calculation
    Ar_37_m = data[1, 0]
    Ar_37_m_std = data[1, 1]
    Ar_37_Ca = Ar_37_m
    Ar_37_Ca_std = Ar_37_m_std

    Ar_36_m = data[0, 0]
    Ar_36_m_std = data[0, 1]
    Ar_36_Ca = Ar_37_Ca * constants[2]
    Ar_36_Air = Ar_36_m - Ar_36_Ca

    Ar_39_m = data[3, 0]
    Ar_39_m_std = data[3, 1]
    Ar_39_Ca = Ar_37_Ca * constants[0]
    Ar_39_Ca_std = (Ar_37_Ca_std/Ar_37_Ca + constants[1]/constants[0]) * Ar_39_Ca
    Ar_39_K = Ar_39_m - Ar_39_Ca
    Ar_39_K_std = minusSigma(Ar_39_m_std, Ar_39_Ca_std)

    Ar_40_m = data[4, 0]
    Ar_40_m_std = data[4, 1]
    Ar_40_air = Ar_36_Air * constants[10]
    Ar_40_K = Ar_39_K * constants[4]
    Ar_40_radioactive = Ar_40_m - Ar_40_air - Ar_40_K
    
    Ar_39_K_40_r_ratio =  Ar_40_radioactive/Ar_39_K
    
    C1, C2, C4 = constants[10], constants[2], constants[0]
    G = Ar_40_m / Ar_39_m
    G_std = G*(Ar_40_m_std/Ar_40_m + Ar_39_m_std/Ar_39_m)
    B = Ar_36_m / Ar_39_m
    B_std = B*(Ar_36_m_std/Ar_36_m + Ar_39_m_std/Ar_39_m)
    D = Ar_37_m / Ar_39_m
    D_std = D*(Ar_37_m_std/Ar_37_m + Ar_39_m_std/Ar_39_m)
    F_std = np.sqrt(G_std**2 + (C1*B_std)**2 + ((C4*G - C1*C4*B + C1*C2)*D_std)**2)
    
    # J calcuation
    J = (np.exp(l*t)-1)/(Ar_40_radioactive/Ar_39_K) 
    v1 = l_std**2*(t*np.exp(l*t)/Ar_39_K_40_r_ratio)**2
    v2 = t_std ** 2 * (l * np.exp(l * t) / Ar_39_K_40_r_ratio) ** 2
    v3 = F_std ** 2 * ((np.exp(l * t)) - 1 / Ar_39_K_40_r_ratio ** 2) ** 2
    J_std = pow(v1 + v2 + v3, 0.5)
    J_int = pow(v3, 0.5)
    return [Ar_36_Air,Ar_37_Ca,Ar_39_K,Ar_40_radioactive,Ar_40_radioactive/Ar_40_m*100,Ar_39_K/Ar_39_m*100,(Ar_39_K*0.52)/Ar_37_Ca,((Ar_39_K*0.52)/Ar_37_Ca)*(Ar_39_K_std/Ar_39_K + Ar_37_Ca_std/Ar_37_Ca + 0.02/0.52),J,J_std,J_int]

def calcAge(measurement_filename, J, J_std, J_int, constants):
    # collect data
    data = np.zeros((5, 2))

    with open(measurement_filename, 'r') as f:
        tmp_data = f.readlines()
    
    # check header here
    if tmp_data[0].rstrip() != "Samp#,t,Min,iradiation PK 90%,Mass,Raw,Measurment,Measurement's Sigma,Ratio,Value,Ratio's Sigma":
        raise Exception("Wrong data format!")

    info = (tmp_data[1].split(',')[0])
    t = (tmp_data[1].split(',')[1])
    Min = (tmp_data[1].split(',')[2])
    PK = (tmp_data[1].split(',')[3])
    
    for i in range(5):
        data[i, 0] = float(tmp_data[i+1].split(',')[6])
        data[i, 1] = float(tmp_data[i+1].split(',')[7])

    # Ar component calculation
    Ar_37_m = data[1, 0]
    Ar_37_m_std = data[1, 1]
    Ar_37_Ca = Ar_37_m
    Ar_37_Ca_std = Ar_37_m_std

    Ar_36_m = data[0, 0]
    Ar_36_m_std = data[0, 1]
    Ar_36_Ca = Ar_37_Ca * constants[2]
    Ar_36_Ca_std = (Ar_37_Ca_std/Ar_37_Ca + constants[3]/constants[2]) * Ar_36_Ca
    Ar_36_Air = Ar_36_m - Ar_36_Ca
    Ar_36_Air_std = minusSigma(Ar_36_m_std, Ar_36_Ca_std)

    Ar_39_m = data[3, 0]
    Ar_39_m_std = data[3, 1]
    Ar_39_Ca = Ar_37_Ca * constants[0]
    Ar_39_Ca_std = (Ar_37_Ca_std/Ar_37_Ca + constants[1]/constants[0]) * Ar_39_Ca
    Ar_39_K = Ar_39_m - Ar_39_Ca
    Ar_39_K_std = minusSigma(Ar_39_m_std, Ar_39_Ca_std)

    Ar_38_m = data[2, 0]
    Ar_38_m_std = data[2, 1]
    Ar_38_K = Ar_39_K * constants[6]
    Ar_38_K_std = (Ar_39_K_std/Ar_39_K + constants[7]/constants[6]) * Ar_38_K
    Ar_38_Air = Ar_38_m - Ar_38_K
    Ar_38_Air_std = minusSigma(Ar_38_m_std, Ar_38_K_std)

    Ar_40_m = data[4, 0]
    Ar_40_m_std = data[4, 1]
    Ar_40_air = Ar_36_Air * constants[10]
    Ar_40_air_std = (Ar_36_Air_std/Ar_36_Air + constants[11]/constants[10]) * Ar_40_air
    Ar_40_K = Ar_39_K * constants[4]
    Ar_40_K_std = (Ar_39_K_std/Ar_39_K + constants[5]/constants[4]) * Ar_40_K
    Ar_40_radioactive = Ar_40_m - Ar_40_air - Ar_40_K
    Ar_40_radioactive_std = np.sqrt(Ar_40_m_std**2 + Ar_40_air_std**2 + Ar_40_K_std**2)
    Ar_40_radioactive_ratio = Ar_40_radioactive / data[4, 0]


    # ratio calculation
    Ar_39_K_40_r_ratio =  Ar_39_K / Ar_40_radioactive
    Ar_39_K_40_r_ratio_std = Ar_39_K_40_r_ratio*(Ar_39_K_std/Ar_39_K + Ar_40_radioactive_std/Ar_40_radioactive)
    Ar_36_Air_40_r_ratio = Ar_36_Air / Ar_40_radioactive
    Ar_36_Air_40_r_ratio_std = Ar_36_Air_40_r_ratio*(Ar_36_Air_std/Ar_36_Air + Ar_40_radioactive_std/Ar_40_radioactive)
    Ar_39_K_36_Air = Ar_39_K / Ar_36_Air
    Ar_39_K_36_Air_std = Ar_39_K_36_Air*(Ar_39_K_std/Ar_39_K + Ar_36_Air_std/Ar_36_Air)

    # Age calculation
    C1, C2, C3, C4 = constants[10], constants[2], constants[4], constants[0]
    G = Ar_40_m / Ar_39_m
    G_std = G*(Ar_40_m_std/Ar_40_m + Ar_39_m_std/Ar_39_m)
    B = Ar_36_m / Ar_39_m
    B_std = B*(Ar_36_m_std/Ar_36_m + Ar_39_m_std/Ar_39_m)
    D = Ar_37_m / Ar_39_m
    D_std = D*(Ar_37_m_std/Ar_37_m + Ar_39_m_std/Ar_39_m)
    F = Ar_40_radioactive / Ar_39_K
    F_std = np.sqrt(G_std**2 + (C1*B_std)**2 + ((C4*G - C1*C4*B + C1*C2)*D_std)**2)

    T = np.log(1 + J*F) / constants[14]
    T_std = np.sqrt((J**2 * F_std**2 + F**2 * J_std**2)/ ((constants[14]*(1+F*J))**2))
    T_int = np.sqrt((J**2 * F_std**2 + F**2 * J_int**2)/ ((constants[14]*(1+F*J))**2))

    return [Ar_36_m, Ar_36_m_std, Ar_36_Air, Ar_36_Air_std, Ar_36_Ca, Ar_36_Ca_std,
            Ar_37_m, Ar_37_m_std, Ar_37_Ca, Ar_37_Ca_std,
            Ar_38_m, Ar_38_m_std, Ar_38_Air, Ar_38_Air_std, Ar_38_K, Ar_38_K_std,
            Ar_39_m, Ar_39_m_std, Ar_39_K, Ar_39_K_std, Ar_39_Ca, Ar_39_Ca_std,
            Ar_40_m, Ar_40_m_std, Ar_40_radioactive, Ar_40_radioactive_std, Ar_40_air, Ar_40_air_std, Ar_40_K, Ar_40_K_std,
            Ar_39_K_40_r_ratio, Ar_39_K_40_r_ratio_std, Ar_36_Air_40_r_ratio, Ar_36_Air_40_r_ratio_std, Ar_39_K_36_Air, Ar_39_K_36_Air_std,
            F, F_std, G, G_std, B, B_std, D, D_std,
            J, J_std,
            T, T_std,
            J_int, T_int,
            Ar_40_radioactive_ratio, C1, C2, C3, C4,info,t,Min,PK
            ]
    
if __name__ == "__main__":

    print(calculateT0(1, filepath='./Data/AS20210429a'))
    #getT0Statistics(["./Data/AS20210429a.csv", "./Data/AS20210429b.csv", "./Data/AS20210429c.csv"])
    #print(getAirRatioStatistics(["./Data/ratio_a.csv", "./Data/ratio_b.csv", "./Data/ratio_c.csv"]))
    #print(calculateMassRatio("./Data/AS20210429a", "./Data/pb20210429a"))
    #print("test")