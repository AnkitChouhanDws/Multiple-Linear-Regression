# What is Regression?
***

- Regression takes a group of random variables, thought to be predicting Y, and tries to find a mathematical relationship between them. 
- This relationship is typically in the form of a straight line (linear regression) that best approximates all the individual data points.

Read more: Regression https://www.investopedia.com/terms/r/regression.asp#ixzz5OA1H851T 
Follow us: Investopedia on Facebook

# What is Multiple Linear Regression?
***
Linear Regression can be of different types as:
- <font color= 'blue'>Simple Linear Regression</font>
- <font color= 'blue'>Multiple Linear Regression</font>

Here we will only discuss about Multiple Linear Regression.<br>
Multiple linear regression is a statistical method that allows us to summarize and study relationships between several continuous (quantitative) variables:
<br>
This variables are of 2 types:
1. Independent variable
2. Dependent variable

Independent variables, denoted as x<sub>0</sub>,x<sub>1</sub>,x<sub>2</sub>,x<sub>3</sub>......x<sub>n</sub> are also regarded as the predictor or explanatory variable.
The dependent variable, denoted as y is regarded as the response or outcome variable.
y<sup>^</sup><sub>i</sub> = b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub> + b<sub>2</sub>x<sub>2</sub> + b<sub>3</sub>x<sub>3</sub>.... + b<sub>n</sub>x<sub>n</sub>

Therfore, we can observe that on variating the values of independent variables, our dependent variables changes.<br>
But think for a while, is this case for all independent variables? Answer is Yes, change in any independent variable changes value of dependent variable.
<br>
Although some alters less and some alters more. <br>

### What if we consider all the independent variables in our regressor?
- Suppose we have 'n' independent variables then total number of models will be-> 2<sup>n</sup> - 1. And if n is large, then it is going to be a large number.
<br>
To avoid this, we have to consider only those independent variables who affect the output above a significance level.
<br><br>
Well, there are techniques through which we can select only the necessary independent variables- <br>
- All-in<br>
- Backward Elimination<br>
- Forward Selection<br>
- Bidirectional elimination<br>
- Score Comparison<br>
(Methods 2,3 and 4 are also called "Stepwise Regression" )<br>
But here we will use only backward elimination. 

### Steps used in Backward elimination approach
***
1. Select a significance level to stay in the model(Let's say s)<br>
2. FIt the full model wuth all possible predictors<br>
3. Consider the predictor with the highest P-value. If P > s, go to Step 4, other finalise the model<br>
4. Remove the predictor<br>
5. Fit model without this variable<br>
6. Repeat the steps 3-5 until model is finalized.<br>

#### For more details, go through the code. Each comment describes the method's working and other useful concepts.





