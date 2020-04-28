import matplotlib.pyplot as plt

sns.lmplot(x='Attack', y='Defense', data=df)

1
2
3
4
	
# Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage

6
7
8
	
# Plot using Seaborn
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, 
           hue='Stage')
 
# Tweak using Matplotlib
plt.ylim(0, None)
plt.xlim(0, None)

sns.boxplot(data=df)

sns.violinplot(x='Type 1', y='Attack', data=df)

sns.swarmplot(x='Type 1', y='Attack', data=df)




# overlay
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=df, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')




melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat") # Name of melted variable
melted_df.head()


sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')


2
3
4
5
	
# Calculate correlations
corr = stats_df.corr()
 
# Heatmap
sns.heatmap(corr)




sns.distplot(df.Attack)
plt.axvline(0, color="k", linestyle="--");




g = sns.factorplot(x='Type 1', 
                   y='Attack', 
                   data=df, 
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot


sns.jointplot(x='Attack', y='Defense', data=df)



sns.kdeplot(df.Attack, df.Defense)



sns.pairplot(iris, hue='species', size=2.5)


grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15));




g = sns.factorplot("day", "total_bill", "sex", data=tips, kind="box")




    sns.violinplot("age_dec", "split_frac", hue="gender", data=data,
                   split=True, inner="quartile",
                   palette=["lightblue", "lightpink"]);


    