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
According to Maeil Business Newspaper, 1169 million accounts are permanently banned in a
single game (PUBG), in a single year (2018). It is estimated that the loss due to cheating
programs is about 2.43 trillion won.
Although companies are developing powerful anti-cheats, they are usually heavy, meaning
that applying them to every player would cause game degradation. Hence, light cheat-
detecting program is urgent to free players from stress caused by cheaters and save the
game industry.

## Goals
In this project, authors developed a probabilistic approach for detecting abnormal players.
Unlike other anti-cheat programs, it can successfully detect abnormal players without
requiring large number of data and need for enormous amount of computation. All this
method demands are the performance data of players, which can be easily calculated by the
equation given in the ‘Solution Method’ section.
Applying this methodology, companies can vastly reduce targets for anti-cheat programs.
Reduced number of anti-cheat appliance will lead to thorough investigation of suspects and
to huge speed up of games, which means that players can enjoy games without stress.

## Probabilistic Model
### System model:
As a model for our project, we chose PUBG since it is widely known FPS game mainly
focused on traditional shooting. Its popularity allows us to model random variable as
following the Gaussian distribution and simplicity reduces additional works to model the
game.
### Random variable:
Performance metric of each player in a match that is calculated using the equation
expressed below.

>>>를 위와 같이 정의한 이유: 한 게임 내에서 100명의 플레이어들의 performance들을

RV의 Sample들로 두고, 그 PMF에서 인 를 가지는 Player들을 candidates로 둔다.
>>>이때, 핵 유저는 해당 게임 내의 평범한 유저들에 비해 비정상적으로 높은 데미지,
헤드샷 비율, 킬 수, 최장 거리 킬, K/D를 기록할 것이다. 따라서, 이들 5가지 지표들을
통해 핵 유저들을 감지할 수 있는 ‘Performace, 를 위와 같이 정의할 수 있다. (각
지표가 0에서 1의 값을 가질 것이고, 총 5가지 지표를 전체 5로 나눌 것이므로 는
0에서 1의 값을 가지게 된다.)
>>>Value of c 정의: (X is performance variable defined in the pool of whole users.)
Value of c is the actually a constant which one of the value of X. In the pool of whole
user, the 3% users of having highest performance will be treated as candidate of
improper user.)

>>>수정이 필요해 보인다 + 이 식이 왜 나왔는지도 적자 Performance를 상대적으로
정의할 수는 없을까? Performance의 평균이 계속 마음에 걸린다. 바로 전판과의 실력
차이도 넣자
σ: Deviation of X
- Assumption:
1) X ~ N(m, σ) =&gt; m값을 정할 수 있어야해용…..
Average number of concurrent users is above 50,000. Thus, approximating the
probability density function of performance as a Gaussian distribution is reasonable
due to the Central Limit Theorem.
2) σ of N(m, σ) is a random variable.
Since players’ performance fluctuate randomly, considering σ as a constant is
obviously misleading. But since fluctuations eventually cancel out in a linear manner,
we can think of mean as a constant.
3) A priori pdf of σ is ….?
이건 정해야 된다
4) 5% of people in terms of performance are considered “abnormal players”.
이것도 지금까지 밴 당한 사람하고 플레이어 수 고려해서 정해야됨
- Mathematical translation:
Given sampled data vector X=[x1, x2, …, xn] and a priori pdf fσ(σ), estimate if a player is
in top 5% of the performance distribution.

## Solution Method
### Estimation of fσ(σ)
By the Bayes’ theorem, a posteriori pdf .
Since the sample data X i follows the Gaussian distribution
