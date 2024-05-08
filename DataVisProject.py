import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

#Page layout
st.set_page_config(layout = 'wide')
st.title("Sports Betting Statistics in the United States")

#Load data
df = pd.read_excel("sports betting stats.xlsx")
percentage_of_bettors = pd.read_excel("numberofbettors.xlsx")
sports_demographics = pd.read_excel("demographics.xlsx").dropna()
revenue = pd.read_excel("revenue2.xlsx").dropna()

#Select what state the user wants
all_states = sorted(df["State"].unique())
target_states = st.multiselect("Choose target states for visualization",
                               all_states,all_states)
#Filter data by selected state
filtered_df = df[df["State"].isin(target_states)]
filtered_revenue = revenue[revenue['State'].isin(target_states)]
filtered_demographics = sports_demographics[sports_demographics['State'].isin(target_states)]
#Figure Layout
col1, col2 = st.columns([5,5])
col3, col4, col5 = st.columns([4,4,2])

#Uniformed height and width
fig_width = 750
fig_height = 600


# Figure 1
legislation = filtered_df[["State","Full Online","Retail Only","Bill Introduced"]].copy()
legislation['color'] = legislation.apply(
    lambda row: 'Online Gambling Allowed' if row["Full Online"] == 'Yes'
                else ('Retail Gambling Allowed' if row["Retail Only"] == "Yes"
                      else ("Bill Introduced" if pd.notnull(row["Bill Introduced"])
                           else 'No Gambling Allowed')), axis=1)
with col1:
    fig1 = px.choropleth(
        data_frame=legislation,
        locations="State",
        locationmode="USA-states",
        scope='usa',
        color="color", 
        color_discrete_map={'Online Gambling Allowed': 'green',
                            'Retail Gambling Allowed': 'blue', 
                            'Bill Introduced': 'yellow', 
                            'No Gambling Allowed': 'red'},
        labels={'color': 'Gambling Status'},
        title="Gambling Status by State")
    fig1.update_layout(
        legend = dict(
            x=0.5,
            y=-0.1,
            xanchor = 'center',
            orientation ='h'
        )
    )
    fig1.update_layout(width=fig_width, height=fig_height)
    fig1.update_layout(legend_title="Gambling Status", legend=dict(orientation='h', x=0.5, xanchor='center', y=-0.1))
    st.plotly_chart(fig1)

# Figure 2
with col2:
    fig2 = px.bar(filtered_revenue, x = ["2023 Total Handle(Billions)","2023 Revenue(Millions)"], y = "State" ,
             title = "2023 Sports Betting: Revenue and Handle by State",
             labels={'value': 'Amount in Millions','variable': 'Category'},
             barmode = 'group')
    fig2.update_layout(width = fig_width, height = fig_height,
                    xaxis_title = "Amount in Millions",
                      yaxis_title = "State",
                      legend_title = "Category")
    fig2.update_layout(legend_title = "Financial Metrics")
    st.plotly_chart(fig2)
    st.markdown("_Note: 'Handle' refers to the total amount of money wagered by bettors._")


#Figure 3
betting_numbers_long =filtered_demographics.melt(id_vars = ["State"], var_name = "Category", value_name = "Value")
#Creating new dataframe for figures 3 and 4
bet = betting_numbers_long[betting_numbers_long["Category"]!="Total Population"]
bet["Group"] = ["Actual" if "Estimated" not in x else "Estimated" for x in bet["Category"]]
with col3:
    fig3 = px.bar(bet[bet["Group"]=="Actual"], x = "State", y = "Value", color = "Category",
             title = "Population by State and Age Group",
             labels = {'Value':'Count','Category':'Legend'})
    fig3.update_layout(width = fig_width,
                      height = fig_height,
                      yaxis_title = "Population",
                       legend = dict(
                           x=0,
                           y=1,
                           xanchor = 'left',
                           yanchor = 'top',
                       )
                      )
    fig3.update_layout(legend_title = 'Age Groups')
    st.plotly_chart(fig3)


#Figure 4

with col4:
    fig4 = px.bar(bet[bet["Group"]=="Estimated"], x = "State", y = "Value", color = "Category",
             title = "Estimated Sports Bettors by State and Age Group",
             labels = {'Value':'Count','Category':'Legend'})
    fig4.update_layout(width = fig_width,
                       height = fig_height,
                       yaxis_title = "Population",
                       legend = dict(
                           x=0,
                           y=1,
                           xanchor = 'left',
                           yanchor = 'top'
                       )
                      )
    st.plotly_chart(fig4)



with col5:
    fig5 = px.bar(percentage_of_bettors, x = "Age Group", y = "% of Betting Participants",
             title = "Percentage of Sports Bettors by Age Group",
             labels={'variable': 'Age Group','variable': '% of Betting Participants'},
             barmode = 'group')
    fig5.update_layout(xaxis_title = "Age Group",
                       yaxis_title = "% of Betting Participants",
                      width = fig_width,
                      height = fig_height,
                      margin=dict(l=80, r=20, t=40, b=20))
    st.plotly_chart(fig5)
