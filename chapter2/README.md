# Making Recommendations

Uses the following 3 Similarity systems:

- Euclidean Distance Score
- Pearson Correlation Score
- Tanimoto Similarity Score

```
cd chapter2
python
import recommendations

# Get Similarity using Euclidean Distance score
recommendations.sim_distance(recommendations.critics,'Lisa Rose','Gene Seymour')

# Get Similarity using Pearson Correlation score
recommendations.sim_pearson(recommendations.critics,'Lisa Rose','Gene Seymour')

# Get ordered list of people with similar tastes to a given person
recommendations.topMatches(recommendations.critics,'Lisa Rose',n=3)

# Get list of movie recommendations for a given user and their projected score
recommendations.getRecommendations(recommendations.critics,'Toby')
```

Use MovieLens Data

```
reload(recommendations)
prefs=recommendations.loadMovieLens()

# Display user 87's user ratings (userid=80) 
prefs['87']

# Get top 5 recommendations for user 87 
recommendations.getRecommendations(prefs,'87')[0:5]
```
