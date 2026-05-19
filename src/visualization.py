import matplotlib.pyplot as plt
import seaborn as sns

def plot_battery_drain_distribution(df):
    '''Show the distribution of the variable battery drain.'''
    plt.figure(figsize = (10,6))

    sns.histplot(
        df['battery_drain_mah_per_day'],
        bins = 25,
        kde = True
    )
    plt.title('Distribution of Battery Drain')
    plt.xlabel('Battery Drain mah_per_day')
    plt.ylabel('Count')

    plt.tight_layout()
    
    plt.savefig('../images/battery_drain_distribution.png',bbox_inches="tight")
                
    plt.show()
    plt.close()
    
def plot_battery_drain_by_device(df):
    
    '''Boxplot of battery drain distribution for each mobile device.'''
    
    plt.figure(figsize = (10,6))
    
    sns.boxplot(
        x= 'device_model',
        y ='battery_drain_mah_per_day',
        data = df
    )
    
    plt.title('Battery Drain by Device Model')
    plt.xlabel('Device Model')
    plt.ylabel('Battery Drain mah_per_day')
    
    plt.xticks(rotation = 15)
    
    plt.tight_layout()
                
    plt.savefig('../images/battery_drain_by_device.png',bbox_inches="tight")            
                
    plt.show()
    plt.close()
    
def plot_battery_drain_by_gender(df):
    
    '''Boxplot of battery drain distribution for each mobile device.'''
    
    plt.figure(figsize=(10,6))

    sns.boxplot(
        x='gender',
        y='battery_drain_mah_per_day',
        data=df
    )

    plt.title('Battery Drain by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Battery Drain mah_per_day')

    plt.tight_layout()
    
    plt.savefig('../images/battery_drain_by_gender.png',bbox_inches="tight")
    
    plt.show()
    plt.close()

def plot_phone_market_share(df):
    
    '''Telephone market share by the 5 phone model device.'''

    device_counts = df['device_model'].value_counts()

    plt.figure(figsize=(7,7))

    plt.pie(
        device_counts,
        labels=device_counts.index,
        autopct='%1.1f%%'
    )

    plt.title('Share of Mobile Market by Device')

    plt.tight_layout()
    
    plt.savefig('../images/phone_market_share.png',bbox_inches="tight")
    
    plt.show()
    plt.close()
    

def plot_user_behavior_class(df):

    '''Plot app usage statistics by user behavior class.'''

    user_class = (
        df.groupby('user_behavior_class')
        .agg({
            'app_usage_time_min_per_day': ['count', 'sum', 'mean']
        })
    )

    user_class.columns = ['count', 'sum', 'mean']

    user_class = user_class.reset_index()

    plt.figure(figsize=(12, 6))

    # Mean App Usage
    plt.subplot(1, 3, 1)

    sns.barplot(
        x='user_behavior_class',
        y='mean',
        data=user_class,
        palette='viridis'
    )

    plt.title('Mean App Usage Time')
    plt.ylabel('Mean App Usage Time')
    plt.xlabel('User Behavior Class')

    # Count of Users
    plt.subplot(1, 3, 2)

    sns.barplot(
        x='user_behavior_class',
        y='count',
        data=user_class,
        palette='viridis'
    )

    plt.title('Count of Users')
    plt.ylabel('Count')
    plt.xlabel('User Behavior Class')

    # Total App Usage
    plt.subplot(1, 3, 3)

    sns.barplot(
        x='user_behavior_class',
        y='sum',
        data=user_class,
        palette='viridis'
    )

    plt.title('Total App Usage Time')
    plt.ylabel('Total Usage Time')
    plt.xlabel('User Behavior Class')

    plt.tight_layout()

    plt.savefig(
        '../images/user_behavior_apps_usage.png',
        bbox_inches='tight'
    )

    plt.show()
    plt.close()

def plot_correlation_heatmap(df):
    
    '''Plot correlation Heatmap of the Variables.'''

    corr_data = df.drop(
        columns=['user_id', 'user_behavior_class']
    )

    plt.figure(figsize=(10,6))

    sns.heatmap(
        corr_data.select_dtypes(include ='number').corr(),
        annot=True,
        fmt='.2f',
        cmap='coolwarm',
        linewidths=0.5
    )

    plt.title('Correlation Heatmap of Mobile User Variables')

    plt.tight_layout()
    
    plt.savefig('../images/correlation_heatmap.png',bbox_inches="tight")
    
    plt.show()
    plt.close()
                
                
                
                
                
                