# ref : https://docs.google.com/document/d/1kRWPEzCqavLgT0xMTLE4YudeHkO9DlhJ2ES5icu84aA/edit
# ref : https://www.desiqna.in/15661/zs-associates-oa-august-2023-freshers-monica-and-dishes
# ZS OA ONCAMPUS

# Monica has cooked n dishes and collected the data on the level of satisfaction for all the dishes from a guest.
# The guest returns an array, where the ith element of the array is the liking level of the ith dish.
# Also, the time taken to cook the ith dish is i. Like-to-time coefficient of a dish is calculated by multiplying the time taken to cook food with its liking level, i.e., input 2[i].
# Total like-to-time coefficient is calculated by summing up all individual coefficients of dishes.
# You want the total like-to-time coefficient to be maximum.
# You can also remove some dishes, in which case, a new coefficient is calculated using the left dishes.
# Find the maximum sum of all possible like-to-time coefficients.

# Eg.
# n = 3
# A = [-1,3,4]

# 1*-1 + 2*3 + 3*4 = 17
# If we exclude -1,
# Then 1*3 + 2*4 = 11
# So, 17 is Max total.

