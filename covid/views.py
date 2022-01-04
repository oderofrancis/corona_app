from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
import pandas as pd

# Create your views here.

# global links

# confirmed=r'/media/afroteop/da442186-249a-498d-9496-21fc43465d5f/corona/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/csse_covid_19_time_series_confirmed_global.csv'
# death=r'/media/afroteop/da442186-249a-498d-9496-21fc43465d5f/corona/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

confirmed=r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
death=r'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

# Continents 

data_csv = pd.read_csv(r'/media/afroteop/da442186-249a-498d-9496-21fc43465d5f/corona/rona/Countries-Continents.csv')

# population

africa_pop = 1388802980
asia_pop = 4700643101
europe_pop = 748321182
south_america_pop = 662730850
north_america_pop = 372283126
oceania_pop = 43500348

total = (africa_pop + asia_pop + south_america_pop + north_america_pop + oceania_pop + europe_pop)



def comment(request):

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for your TIME...      PAMOJA TUKOMESHE CORONA')
            return redirect('world')

        else:
            return redirect('comment')

    context = {'form':form}


    return render(request,'user/comment.html',context)

def world(request):

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)
    

    # data analysis

                # confirmed         
    totalconfirmed = data_confirmed[data_confirmed.columns[-1]].sum()
    alldata = len(data_confirmed)
    total_mean = (totalconfirmed/alldata)
    total_mean = round(total_mean)
    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']
    data_confirmed = data_confirmed.sort_values(by='confirmed',ascending=False).head(50)
    data_confirmed_values = data_confirmed['confirmed'].values.tolist()
    data_confirmed_names = data_confirmed['Country/Region'].values.tolist()

                # death
    totaldeath = data_death[data_death.columns[-1]].sum()
    alldeath = len(data_death)
    total_mean_death = (totaldeath/alldeath)
    total_mean_death = round(total_mean_death)
    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','death']
    data_death = data_death.sort_values(by='death',ascending=False).head(50)
    data_death_values = data_death['death'].values.tolist()
    data_death_names = data_death['Country/Region'].values.tolist()

    # ratios

    spread_rate = (totalconfirmed / total)*100
    spread_rate = round(spread_rate,2)

    death_rate = (totaldeath / totalconfirmed)*100
    death_rate = round(death_rate,2)

    context = {
    # confirmed
    'totalconfirmed':totalconfirmed,
    'alldata':alldata,
    'total_mean':total_mean,
    'data_confirmed_values':data_confirmed_values,
    'data_confirmed_names':data_confirmed_names,
    # death
    'totaldeath':totaldeath,
    'alldeath':alldeath,
    'total_mean_death':total_mean_death,
    'data_death_values':data_death_values,
    'data_death_names':data_death_names,

    # rates
    'spread_rate':spread_rate,
    'death_rate':death_rate,
    
    }

    return render(request,'continents/world.html',context)

def n_america(request):
    # data reading

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)

    # data analysis

    # confirmed cases

    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']


    # merging the two data
    data_merge = pd.merge(right=data_csv, left=data_confirmed,
                        how='left', right_on='Country', 
                        left_on='Country/Region')

    north_america = data_merge[data_merge['Continent']=='North America']
    all_north_america = len(north_america)
    north_america_total = north_america[north_america.columns[1]].sum()
    north_america_mean = round((north_america_total/all_north_america))
    north_america  = north_america[['Country/Region',north_america .columns[1]]].groupby('Country/Region').sum()
    north_america  = north_america.reset_index()
    north_america  = north_america.sort_values(by='confirmed',ascending=False)
    north_america_values = north_america['confirmed'].values.tolist()
    north_america_names = north_america['Country/Region'].values.tolist()

    
    # death cases

    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','death']

   # merging the two data
    data_merge_death = pd.merge(right=data_csv, left=data_death,
                             how='left', right_on='Country', 
                             left_on='Country/Region'
                             )

    north_america_death = data_merge_death[data_merge_death['Continent']=='North America']
    all_north_america_death = len(north_america_death)
    north_america_death_total = north_america_death[north_america_death.columns[1]].sum()
    north_america_death_mean = round((north_america_death_total/all_north_america_death))
    north_america_death = north_america_death[['Country/Region',north_america_death.columns[1]]].groupby('Country/Region').sum()
    north_america_death = north_america_death.reset_index()
    north_america_death.columns=['Country/Region','death']
    north_america_death = north_america_death.sort_values(by='death',ascending=False)
    north_america_death_values = north_america_death['death'].values.tolist()
    north_america_death_names = north_america_death['Country/Region'].values.tolist()

    # north pop


    north_america_spread_rate = (north_america_total / north_america_pop )*100
    north_america_spread_rate = round(north_america_spread_rate,2)

    north_america_death_rate = (north_america_death_total / north_america_total)*100
    north_america_death_rate = round(north_america_death_rate,2)

    context = {
    # confirmed
    'north_america_total':north_america_total,
    'all_north_america':all_north_america,
    'north_america_mean':north_america_mean,
    'north_america_values':north_america_values,
    'north_america_names':north_america_names,

    # death
    'north_america_death_total':north_america_death_total,
    'all_north_america_death':all_north_america_death,
    'north_america_death_mean':north_america_death_mean,
    'north_america_death_values':north_america_death_values,
    'north_america_death_names':north_america_death_names,

    # rates
    'north_america_spread_rate':north_america_spread_rate,
    'north_america_death_rate':north_america_death_rate
    }
    return render(request,'continents/n_america.html',context)

def s_america(request):

    # data reading

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)

    # data analysis

    # confirmed cases

    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']

    # confirmed cases

    # merging the two data
    data_merge = pd.merge(right=data_csv, left=data_confirmed,
                        how='left', right_on='Country', 
                        left_on='Country/Region')

    south_america = data_merge[data_merge['Continent']=='South America']
    all_south_america = len(south_america)
    south_america_total = south_america[south_america.columns[1]].sum()
    south_america_mean = round((south_america_total/all_south_america))
    south_america  = south_america [['Country/Region',south_america .columns[1]]].groupby('Country/Region').sum()
    south_america  = south_america .reset_index()
    south_america.columns=['Country/Region','confirmed']
    south_america  = south_america .sort_values(by='confirmed',ascending=False)
    south_america_values = south_america ['confirmed'].values.tolist()
    south_america_names = south_america ['Country/Region'].values.tolist()


    # death

        # death cases

    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','death']

    data_csv_death = pd.read_csv(r'https://raw.githubusercontent.com/oderofrancis/rona/main/Countries-Continents.csv')
    # merging the two data
    data_merge_death = pd.merge(right=data_csv, left=data_death,
                             how='left', right_on='Country', 
                             left_on='Country/Region'
                             )
    south_america_death = data_merge_death[data_merge_death['Continent']=='South America']
    all_south_america_death = len(south_america_death)
    south_america_death_total = south_america_death[south_america_death.columns[1]].sum()
    south_america_death_mean = round((south_america_death_total/all_south_america_death))
    south_america_death = south_america_death[['Country/Region',south_america_death.columns[1]]].groupby('Country/Region').sum()
    south_america_death = south_america_death.reset_index()
    south_america_death.columns=['Country/Region','death']
    south_america_death = south_america_death.sort_values(by='death',ascending=False)
    south_america_death_values = south_america_death['death'].values.tolist()
    south_america_death_names = south_america_death['Country/Region'].values.tolist()

    # rates

    south_america_spread_rate = (south_america_total / south_america_pop )*100
    south_america_spread_rate = round(south_america_spread_rate,2)

    south_america_death_rate = (south_america_death_total / south_america_total)*100
    south_america_death_rate = round(south_america_death_rate,2)

    context = {
    # confirmed
    'south_america_total':south_america_total,
    'all_south_america':all_south_america,
    'south_america_mean':south_america_mean,
    'south_america_values':south_america_values,
    'south_america_names':south_america_names,

    # death
    'south_america_death_total':south_america_death_total,
    'all_south_america_death':all_south_america_death,
    'south_america_death_mean':south_america_death_mean,
    'south_america_death_values':south_america_death_values,
    'south_america_death_names':south_america_death_names,

    # rates
    'south_america_spread_rate':south_america_spread_rate,
    'south_america_death_rate':south_america_death_rate
    }

    return render(request,'continents/s_america.html',context)

def asia(request):

    # data reading

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)

    # data analysis

    # confirmed cases

    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']


    # merging the two data
    data_merge = pd.merge(right=data_csv, left=data_confirmed,
                        how='left', right_on='Country', 
                        left_on='Country/Region')

    # confirmed cases

    asia = data_merge[data_merge['Continent']=='Asia']
    # len
    all_asia = len(asia)
    # sum
    asia_total = asia[asia.columns[1]].sum()
    # mean
    asia_mean = round((asia_total/all_asia))
    asia = asia[['Country/Region',asia.columns[1]]].groupby('Country/Region').sum()
    asia = asia.reset_index()
    asia = asia.sort_values(by='confirmed',ascending=False)
    asia_values = asia['confirmed'].values.tolist()
    asia_names = asia['Country/Region'].values.tolist()

    # death

    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','death']

    # merging the two data
    data_merge_death = pd.merge(right=data_csv, left=data_death,
                             how='left', right_on='Country', 
                             left_on='Country/Region'
                             )

    asia_death = data_merge_death[data_merge_death['Continent']=='Asia']
    all_asia_death = len(asia_death)
    asia_death_total = asia_death[asia_death.columns[1]].sum()
    asia_death_mean = round((asia_death_total/all_asia_death))
    asia_death = asia_death[['Country/Region',asia_death.columns[1]]].groupby('Country/Region').sum()
    asia_death = asia_death.reset_index()
    asia_death.columns=['Country/Region','death']
    asia_death = asia_death.sort_values(by='death',ascending=False)
    asia_death_values = asia_death['death'].values.tolist()
    asia_death_names = asia_death['Country/Region'].values.tolist()

    # rates

    asia_spread_rate = (asia_total / asia_pop )*100
    asia_spread_rate = round(asia_spread_rate,2)

    asia_death_rate = (asia_death_total / asia_total)*100
    asia_death_rate = round(asia_death_rate,2)

    context = {
    # confirmed
    'asia_total':asia_total,
    'all_asia':all_asia,
    'asia_mean':asia_mean,
    'asia_values':asia_values,
    'asia_names':asia_names,

    # death
    'asia_death_total':asia_death_total,
    'all_asia_death':all_asia_death,
    'asia_death_mean':asia_death_mean,
    'asia_death_values':asia_death_values,
    'asia_death_names':asia_death_names,

    # rates
    'asia_spread_rate':asia_spread_rate,
    'asia_death_rate':asia_death_rate
    }
    return render(request,'continents/asia.html',context)

def europe(request):

    # data reading

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)

    # data analysis

    # confirmed cases

    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']

    data_csv = pd.read_csv(r'https://raw.githubusercontent.com/oderofrancis/rona/main/Countries-Continents.csv')

    # merging the two data
    data_merge = pd.merge(right=data_csv, left=data_confirmed,
                        how='left', right_on='Country', 
                        left_on='Country/Region')

    europe = data_merge[data_merge['Continent']=='Europe']
    all_europe = len(europe)
    europe_total = europe[europe.columns[1]].sum()
    europe_mean = round((europe_total/all_europe))
    europe = europe[['Country/Region',europe.columns[1]]].groupby('Country/Region').sum()
    europe = europe.reset_index()
    europe = europe.sort_values(by='confirmed',ascending=False)
    europe_values = europe['confirmed'].values.tolist()
    europe_names = europe['Country/Region'].values.tolist()


    # death

    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','death']

    # merging the two data
    data_merge_death = pd.merge(right=data_csv, left=data_death,
                             how='left', right_on='Country', 
                             left_on='Country/Region'
                             )

    europe_death = data_merge_death[data_merge_death['Continent']=='Europe']
    all_europe_death = len(europe_death)
    europe_death_total = europe_death[europe_death.columns[1]].sum()
    europe_death_mean = round((europe_death_total/all_europe_death))
    europe_death = europe_death[['Country/Region',europe_death.columns[1]]].groupby('Country/Region').sum()
    europe_death = europe_death.reset_index()
    europe_death = europe_death.sort_values(by='death',ascending=False)
    europe_death_values = europe_death['death'].values.tolist()
    europe_death_names = europe_death['Country/Region'].values.tolist()

    # rates

    europe_spread_rate = (europe_total / europe_pop )*100
    europe_spread_rate = round(europe_spread_rate,2)

    europe_death_rate = (europe_death_total / europe_total)*100
    europe_death_rate = round(europe_death_rate,2)

    context = {
    # confirmed
    'europe_total':europe_total,
    'all_europe':all_europe,
    'europe_mean':europe_mean,
    'europe_values':europe_values,
    'europe_names':europe_names,

    # death
    'europe_death_total':europe_death_total,
    'all_europe_death':all_europe_death,
    'europe_death_mean':europe_death_mean,
    'europe_death_values':europe_death_values,
    'europe_death_names':europe_death_names,

    # rates
    'europe_spread_rate':europe_spread_rate,
    'europe_death_rate':europe_death_rate
    }
    return render(request,'continents/europe.html',context)

def africa(request):

    # data reading

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)
    

    # confirmed cases

    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']


    data_merge = pd.merge(right=data_csv, left=data_confirmed,
                        how='left', right_on='Country', 
                        left_on='Country/Region')

    africa = data_merge[data_merge['Continent']=='Africa']
    all_africa = len(africa)
    africa_total = africa[africa.columns[1]].sum()
    africa_mean = (africa_total/all_africa)
    africa_mean = round(africa_mean)
    africa = africa[['Country/Region',africa.columns[1]]].groupby('Country/Region').sum()
    africa = africa.reset_index()
    africa = africa.sort_values(by='confirmed',ascending=False)
    africa_values = africa['confirmed'].values.tolist()
    africa_names = africa['Country/Region'].values.tolist()

    # death analysis

    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','confirmed']

    # merging the two data
    data_merge_death = pd.merge(right=data_csv, left=data_death,
                             how='left', right_on='Country', 
                             left_on='Country/Region'
                             )

    # death

    africa_death = data_merge_death[data_merge_death['Continent']=='Africa']
    #len
    all_africa_death = len(africa_death)
    # sum
    africa_death_total = africa_death[africa_death.columns[1]].sum()
    # mean
    africa_death_mean = (africa_death_total/all_africa_death)
    africa_death_mean = round(africa_death_mean)
    # analysis
    africa_death = africa_death[['Country/Region',africa_death.columns[1]]].groupby('Country/Region').sum()
    africa_death = africa_death.reset_index()
    africa_death.columns=['Country/Region','death']
    africa_death = africa_death.sort_values(by='death',ascending=False)
    africa_death_values = africa_death['death'].values.tolist()
    africa_death_names = africa_death['Country/Region'].values.tolist()

    # africa rates

    africa_spread_rate = (africa_total / africa_pop )*100
    africa_spread_rate = round(africa_spread_rate,2)

    africa_death_rate = (africa_death_total / africa_total)*100
    africa_death_rate = round(africa_death_rate,2)

    context = {
    # confirmed
    'africa_total':africa_total,
    'all_africa':all_africa,
    'africa_mean':africa_mean,
    'africa_values':africa_values,
    'africa_names':africa_names,

    # death
    'africa_death_total':africa_death_total,
    'all_africa_death':all_africa_death,
    'africa_death_mean':africa_death_mean,
    'africa_death_values':africa_death_values,
    'africa_death_names':africa_death_names,

    # rates
    'africa_spread_rate':africa_spread_rate,
    'africa_death_rate':africa_death_rate
    }

    return render(request,'continents/africa.html',context)

def oceania(request):

    # data reading

    data_confirmed = pd.read_csv(confirmed)
    data_death = pd.read_csv(death)

    # data analysis

    # confirmed cases

    data_confirmed = data_confirmed[['Country/Region',data_confirmed.columns[-1]]].groupby('Country/Region').sum()
    data_confirmed = data_confirmed.reset_index()
    data_confirmed.columns=['Country/Region','confirmed']


    # merging the two data
    data_merge = pd.merge(right=data_csv, left=data_confirmed,
                        how='left', right_on='Country', 
                        left_on='Country/Region')


    oceania = data_merge[data_merge['Continent']=='Oceania']
    all_oceania = len(oceania)
    oceania_total = oceania[oceania.columns[1]].sum()
    oceania_mean =round((oceania_total/all_oceania))
    oceania  = oceania [['Country/Region',oceania .columns[1]]].groupby('Country/Region').sum()
    oceania  = oceania .reset_index()
    oceania  = oceania .sort_values(by='confirmed',ascending=False)
    oceania_values = oceania['confirmed'].values.tolist()
    oceania_names = oceania['Country/Region'].values.tolist()

    # death

            # death cases

    data_death = data_death[['Country/Region',data_death.columns[-1]]].groupby('Country/Region').sum()
    data_death = data_death.reset_index()
    data_death.columns=['Country/Region','death']

     # merging the two data
    data_merge_death = pd.merge(right=data_csv, left=data_death,
                             how='left', right_on='Country', 
                             left_on='Country/Region'
                             )

    oceania_death = data_merge_death[data_merge_death['Continent']=='Oceania']
    all_oceania_death = len(oceania_death)
    oceania_death_total = oceania_death[oceania_death.columns[1]].sum()
    oceania_death_mean = round((oceania_death_total/all_oceania_death))
    oceania_death  = oceania_death [['Country/Region',oceania_death.columns[1]]].groupby('Country/Region').sum()
    oceania_death  = oceania_death .reset_index()
    oceania_death  = oceania_death .sort_values(by='death',ascending=False)
    oceania_death_values = oceania_death['death'].values.tolist()
    oceania_death_names = oceania_death['Country/Region'].values.tolist()

    oceania_spread_rate = (oceania_total / oceania_pop )*100
    oceania_spread_rate = round(oceania_spread_rate,2)

    oceania_death_rate = (oceania_death_total / oceania_total)*100
    oceania_death_rate = round(oceania_death_rate,2)


    context = {
    # confirmed

    'oceania_total':oceania_total,
    'all_oceania':all_oceania,
    'oceania_mean':oceania_mean,
    'oceania_values':oceania_values,
    'oceania_names':oceania_names,

    # death
    'oceania_death_total':oceania_death_total,
    'all_oceania_death':all_oceania_death,
    'oceania_death_mean':oceania_death_mean,
    'oceania_death_values':oceania_death_values,
    'oceania_death_names':oceania_death_names,

    # rates
    'oceania_spread_rate':oceania_spread_rate,
    'oceania_death_rate':oceania_death_rate
    }

    return render(request,'continents/oceania.html',context)
