import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import ttest_ind, shapiro, levene, f_oneway

def operating_system_battery_ttest(df):
    
    '''Test whether battery drain differs between Android and iOS.'''
    
    android_sample=df[df['operating_system']=='Android']['battery_drain_mah_per_day']
    ios_sample = df[df['operating_system']== 'iOS']['battery_drain_mah_per_day']
    
    t_stat,p_value = ttest_ind(android_sample, ios_sample)
    
    print('T-statistic: ',t_stat)
    print('P-value: ',p_value)
    
    return t_stat, p_value

def get_device_data_usage_groups(df):
    
    '''Helping function to create data usage groups by device model.'''
    
    groups = {
        device:group['data_usage_mb_per_day']
        for device, group in df.groupby('device_model')
    }
    
    return groups
        
    
def check_normality_histograms(df):
    
    '''Plot histograms to visually check normality for each device model.'''
    
    groups = get_device_data_usage_groups(df)
    
    for device, data in groups.items():
        plt.figure(figsize = (8,5))
        
        sns.histplot(data, bins = 10, kde=True)
        
        plt.xlabel('Data Usage MB/day')
        plt.ylabel('Frequency')
        plt.title(f'Distribution of Data Usage - {device}')
        
        plt.tight_layout()
        plt.show()
        plt.close()
        
def check_normality_qqplots(df):
    
    '''Plot Q-Q plots to visually check normality for each device model.'''
    
    groups = get_device_data_usage_groups(df)
    
    for device, data in groups.items():
        plt.figure(figsize = (8,5))
        
        stats.probplot(data, dist='norm', plot=plt)
        
        plt.title(f'Q-Q. Plot - {device}')
        
        plt.tight_layout()
        plt.show()
        plt.close()
        
def check_shapiro_wilk_test(df):
    
    '''Run Shapiro Wilk normality test for each device model.'''
    
    groups = get_device_data_usage_groups(df)
    
    for device, data in groups.items():
        stat, p = shapiro(data)
        
        print(f'{device}')
        print('Statistic: ',stat)
        print('P-value:', p)
        
        
def check_homogeneity(df):
    
    ''' Run Levine test for equal variances across device models.'''
    
    groups = get_device_data_usage_groups(df)
    
    stat, p = levene(*groups.values())
    
    print('Levine Statistic:', stat)
    print('P-value:', p)
    
    return  stat, p


def device_model_data_usage_anova(df):
    '''Run one way ANOVA for data usage across device models.'''
    
    groups = get_device_data_usage_groups(df)
    
    f_stat, p_value = f_oneway(*groups.values())
    
    print('F-statistic:',f_stat)
    print('P-value:', p_value)
    
    return f_stat, p_value
    
    
    
    
        
    
    
    
        
    
    
 
        