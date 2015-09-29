# Movie rating recommendations

Uses the following two Similarity systems:

- Euclidean Distance Score
- Pearson Correlation Score

```
cd movie-rating-recommendations
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
