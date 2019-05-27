# PUBG_Cheater_Detector

![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

Using PUBG API to detect cheater in game based on probability theories and statistics
Student Project: Nguyen Cong Khang, Kim Jinwoong, Choi Seunghyun - Yonsei University, Department of Electrical and Electronic Engineering

Instructor: Professor Kim Seonglyun / Email: slkim@yonsei.ac.kr

## Installation
This project is using PUBG API tools. To see the documentation of the [PUBG API, click here](https://documentation.pubg.com/en/introduction.html)

A PUBG API key is needed for this project. To obtain the API key, [apply in this link](https://developer.pubg.com/). 
After getting the API key, create a file named "PUBGAPIKEY.txt" and paste the API key in this text file. Then, you can run this source code

This project is working on Linux Machines (specifically in this case we use Ubuntu 18.10)
To check your Ubuntu version, use
```
lsb_release -a
```
Python 3 will be used in this project
To install Python 3, use
```
sudo apt-get install python3
```
To install pip for python3, use
```
sudo apt-get install python3-pip
```
We are using PUBG provided API tool to help crawl users data for this project. Here is the link for PUBG API on Python
[PUBG API - Python](https://github.com/ramonsaraiva/pubg-python)


To install the wrapper, use 'pip3'

```
pip3 install pubg-python
```
## Abstract
Nowadays, online gaming industry is rapidly growing thanks to great games including League
of Legends (LoL), Overwatch, PlayerUnknown’s Battleground(PUBG). Unfortunately, they
severely suffer from cheating programs. Cheating programs allow users to play with great
advantages: automatically shooting enemies, dodging bullets, knowing enemies’ location
without even meeting them.
According to Maeil Business Newspaper 1 , 1169 million accounts are permanently banned in a
single game (PUBG), in a single year (2018). It is estimated that the loss due to cheating
programs is about 2.43 trillion won.
Although companies are developing powerful anti-cheats, they are usually heavy, meaning
that applying them to every player would cause game degradation. Hence, light cheat-
detecting program is urgent to free players from stress caused by cheaters and save the
game industry.

## Goals
In this project, authors developed a probabilistic approach for detecting abnormal players.
Unlike other anti-cheat programs, it can successfully detect abnormal players without
requiring large number of data and need for enormous amount of computation
Applying this methodology, companies can vastly reduce targets for anti-cheat programs.
Reduced number of anti-cheat appliance will lead to thorough investigation of suspects and
to huge speed up of games, which means that players can enjoy games without stress.
The result of a simulation is shown in Appendix B.

## Probabilistic Model
### System model:
As a model for our project, we chose PUBG (Player Unknown's Battleground) since it is widely known FPS game mainly
focused on traditional shooting. Its popularity allows us to model random variable as
following the Gaussian distribution and simplicity reduces additional works to model the
game.
### Random variable:
1./ X: Performance of each player defined as:

We divided each term by the average value since we wanted to normalize the
impact of values. Weights of each term show how important such term is in order to
catch a cheater. Since hackers usually show incredibly high rate of headshot, the
percentage of headshot is weighted the most, followed by the number of kills, the
longest distance of kill, damage, and survival time. In order to keep the value of
performance as simple as possible, we divided the whole term by 37, summation of
each weights.

2./ σ: Deviation of X

- Assumption:
1) X ~ N(m, σ)
Average number of concurrent users is above 50,000. Thus, approximating the
probability density function of performance as a Gaussian distribution is reasonable
due to the Central Limit Theorem.
2)
We assume that the average of the performance X is equal to the average of the
sample performance [X] from one game. This is a plausible assumption since it is
known that the system matches players in almost random way. Hence mean will be
the same as the sampled mean, considering that mean is a linear combination of
random variables. Shown in Appendix A.
3) σ of N(m, σ) is a random variable.
Since players’ performance fluctuate randomly, considering σ as a constant is
obviously misleading. Therefore, we assumed σ to be a random variable.
4) A priori pdf .
For Bayesian estimation, reasonably estimating a priori pdf is extremely important
and hard. Since we don’t have previous data for f, we performed our algorithm
several times and found out that deviation never exceeds 3 and is over 1.5. Shown in
Appendix A
For our algorithm, this pdf is used only at the start of the whole program. As program
get more data, it will update the pdf after each match, allowing the pdf to be closer to
the “true” pdf.
5) Being in top 10% of N(m, σ) means he/she is an abnormal player.
According to Joongang Ilbo 2 , about 18% of players were permanently banned from
the game by April 30, 2018. Since the number of hackers had been constantly
decreasing since then, we assumed that 10% of players are cheaters. Therefore, if a
player is inside 10% of the estimated pdf N(m, σ), he/she is a suspicious player.
- Mathematical translation:
Given a sampled data vector [X]=[x1, x2, …, xn] and a priori pdf fσ(σ), estimate if a
player is in top 10% of the unknown performance distribution N(m, σ).

## Solution Method
1) Get the required data (percentage of headshot, damage done, number of kills, longest
distance of kill, survival time) from the PUBG database.

2) Calculate the performance X for each player given the equation for X as follows.

3) X~N(m, σ)
Since the performance of different players are iid (independently and identically
distributed) and the number of players is large, the performance random variable X
follows the Gaussian distribution with mean m and deviation σ by the central limit
theorem. Given the relation , calculate the mean from the sampled data.

4) Estimation of a posteriori fσ(σ)
By the Bayes’ theorem, a posteriori pdf , since the performance of players is iid.
Since the sample data X i follows the Gaussian distribution , , where n is the number of
players. This relation will be used as fσ(σ|X) because we’re interested in σ that
maximizes the pdf, not the probability of σ itself.

5) Search for the most probable σ
Given a posteriori pdf fσ(σ|X), we find the most probable σ for the distribution of
performance of whole players, so that we can detect players who are in top 10% of the
performance pdf.
If the given data were huge, differentiating the posteriori pdf by σ would have been
considered. However, since the number of the data is no larger than 100, maximum
function (quicksort) is used for the program. Denote σ which is the most probable by σ’
from now on.

6) Find the suspicious players
σ is no longer a random variable, but a constant σ’.
What we have to do is find the threshold value T such that P(X≥T)=0.1.
Since X~N(m, σ’), manipulate the equation into the standard normal distribution form,
P(Z≥=0.1. Hence T=0.1285σ’+m.
Now that we have the threshold performance value T, search for all players above T.
These players are considered as suspicious players.
![image021](https://user-images.githubusercontent.com/15692058/58432892-a8db6380-80ef-11e9-8725-812cde185735.png)
![image020](https://user-images.githubusercontent.com/15692058/58432918-c1e41480-80ef-11e9-9041-5beeffafaaac.png)

