WEBVTT

1
00:00:02.620 --> 00:00:12.819
Jessica: Okay, Hello, everybody, and welcome to the module. 7 office hour for the professional certificate in machine learning. And AI,

2
00:00:13.348 --> 00:00:35.819
Jessica: yeah. So I guess we can start right away. I see some people are still joining before we start. I guess. One thing I want to say is that I have graded the practical application assignments for module 5 for my section.

3
00:00:36.319 --> 00:00:50.291
Jessica: Everybody should have received their grades by then. Obviously, I'm not. Gonna you know, I think the submissions were fine. On average, we're okay on average.

4
00:00:50.970 --> 00:00:54.578
Jessica: I didn't see anything to

5
00:00:55.330 --> 00:01:23.260
Jessica: you know, alarming in sense of oh, like, maybe, like, there is some confusion about a particular topic. So I was happy with that. And but of course, what I want to emphasize is that if you require, or you want more specific feedback about your grade, you are encouraged to contact your learning facilitator, and we're going to be more than

6
00:01:23.260 --> 00:01:27.169
Jessica: happy to to provide you with that. Okay.

7
00:01:28.581 --> 00:01:31.260
Jessica: alright. So I do see

8
00:01:31.970 --> 00:01:34.870
Jessica: some people joining

9
00:01:37.240 --> 00:01:59.250
Jessica: So I guess I can get started with today's material. So today we are learning about the 1st supervised model that you're going to learn in this course. I know last week you have learned K-means, I think, during module 6

10
00:01:59.350 --> 00:02:00.255
Jessica: so

11
00:02:01.980 --> 00:02:25.980
Jessica: or k nearest neighbors, one of the 2 and which was unsupervised. And it was a type of classification algorithm K. Means and dB, scan. Yes, I did not have an office hour, so I did not. I kind of forgot what we were talking about. But yes. So last week you saw your 1st type of classification algorithms. Okay?

12
00:02:25.980 --> 00:02:42.479
Jessica: And this week we are going. I'm going to introduce you to your 1st regression algorithm, which is called linear regression. So I have prepared for today a

13
00:02:43.800 --> 00:02:45.453
Jessica: Jupiter notebook.

14
00:02:46.770 --> 00:03:10.490
Jessica: So this is the one that I will be using today. So I do have an example of multiple of sorry, simple linear regression and multiple linear regression. And yeah, so I guess we can get started. So before we get into the details of you know, like how to implement

15
00:03:10.490 --> 00:03:17.590
Jessica: linear regression in Python, it is important that we sort of like, understand the type of problems that

16
00:03:17.760 --> 00:03:20.800
Jessica: this algorithm can help us solve. Okay.

17
00:03:21.654 --> 00:03:28.439
Jessica: although you won't know right off the bat

18
00:03:28.520 --> 00:03:39.923
Jessica: what algorithm is best to solve your problem. Having an idea of what type of algorithm of problems an algorithm can solve can help you.

19
00:03:40.530 --> 00:03:57.429
Jessica: you know, like, kind of like, select the algorithms that you want to apply to a certain problem. And so that typically you're gonna end up making a comparison of a few different ones and then pick the one that performs best. Okay.

20
00:03:57.620 --> 00:04:01.554
Jessica: so there are many ways of

21
00:04:03.500 --> 00:04:28.260
Jessica: classifying. I guess machine learning algorithms. Okay, one of them ways is to decide is to classify them based on the type of problems that you want to solve. So one of the most common ways is to establish whether you are solving a classification problem or a regression problem. So a classification problem is anything that can be solved

22
00:04:28.310 --> 00:04:41.280
Jessica: with algorithms like K-means and others that we're gonna study later in the course. But is this essentially algorithms where you are given a set of data points.

23
00:04:41.380 --> 00:05:04.270
Jessica: and you want to try and classify these points based on some type of similarity between them. Okay, this could be classify different customers based on their spending patterns, or decide whether you know, like some credit card transactions, are fraudulent or not.

24
00:05:04.270 --> 00:05:24.409
Jessica: based on their usage based on You can also classify whether an email is a spam email or not based on the type of characters that are in it, and so on. So these are type of classification, some examples of classification problems that can be solved with classification algorithms. Okay.

25
00:05:24.450 --> 00:05:37.389
Jessica: there is a whole other set of problems that machine learning can solve that are called regression problems, regression problems are those type of problem that essentially help you

26
00:05:37.390 --> 00:05:59.769
Jessica: predict a certain value of a certain quantity in the future. Okay, so, for example, if you are interested in knowing or trying to understand better what the price of gold would be in 10 years. That would be a good candidate for a regression problem.

27
00:05:59.920 --> 00:06:16.210
Jessica: Okay, obviously, regression problems don't grant you a window to the future. They're not a crystal ball. They don't allow you to know exactly what's going to happen, but you can. But they can give you a predictive idea about what is about to happen with that particular problem.

28
00:06:16.330 --> 00:06:30.169
Jessica: Another example of a regression problem could be predicting the price of a house based on the features of the house. So given a house with, I don't know.

29
00:06:30.170 --> 00:06:51.380
Jessica: 1,000 square feet and 3 bedrooms and a detached garage. For example, you can try and ballpark or predict. Okay, the price of the house based on other houses that are in the same neighborhood or in the same city. Okay?

30
00:06:52.499 --> 00:06:57.890
Jessica: Other examples of regression problems could be like inventory

31
00:06:57.930 --> 00:07:18.833
Jessica: problems. Okay? So if you're trying to stock up your inventory for your business and try and figure out how much of each product you should buy. That is a typical example of a regression problem. Okay? So it's very, very important that whenever you are presented with a data science question, you sort of like,

32
00:07:19.880 --> 00:07:21.680
Jessica: establish

33
00:07:21.710 --> 00:07:43.189
Jessica: what type of problem that is okay, is it going to be a classification problem? It is going to be a regression problem. Or is it going to be something else? Okay, that we're going to see later in the course, such as natural language processing, reinforcement, learning, and all that. Okay. But classification and regression are the 2 main ones, and once you make that

34
00:07:45.400 --> 00:08:02.290
Jessica: once you understand the difference. Okay? And you establish to which category your problem belongs to, it's very easy for you to. It's going to be easy for you to sort of like, pick the algorithms that you can apply. Okay, if you have a regression problems.

35
00:08:02.410 --> 00:08:10.579
Jessica: all the classification algorithms get automatically discarded. They're not gonna work for your problem. They're not suited for that problem. And vice versa.

36
00:08:10.910 --> 00:08:11.625
Jessica: Okay.

37
00:08:14.220 --> 00:08:31.790
Jessica: so I am going to skip talking about the math behind linear regression, just because it is very well done in the videos by the faculty. Okay, it's not also not extremely complicated. The reason why linear regression is

38
00:08:32.070 --> 00:08:39.880
Jessica: almost always thought as like thought as a 1st machine learning algorithm out there

39
00:08:39.890 --> 00:09:01.119
Jessica: is because its foundations are on 2 very simple mathematical concept. One is the equation of the line and the other one is something called ordinarily squares, which is a technique to compute the distance of a line from points. Okay? So there's nothing

40
00:09:01.140 --> 00:09:22.807
Jessica: very complicated behind the math of linear regression, but its simplicity is fascinating because you can. You are going to see that, you know, like, throughout the module and throughout the course that is to this day one of the main regression algorithms that are used out there. Okay?

41
00:09:23.580 --> 00:09:31.260
Jessica: there are 2 main types of linear regressions. Okay.

42
00:09:31.370 --> 00:09:50.050
Jessica: there is a simple linear regression or single linear regression. And there are, there is multiple linear regression. And what is the difference between them? Well, let's consider this small table that I have here. Okay, so

43
00:09:50.684 --> 00:10:15.899
Jessica: like, for any machine learning algorithm, what you're going to need is one or more input variable. Okay, that you pass to your algorithm itself and that you use in order to try to predict a certain output. Y, okay, so in this, this example of this table that I have here on the screen.

44
00:10:15.940 --> 00:10:19.239
Jessica: the output or the quantity that we

45
00:10:19.370 --> 00:10:22.300
Jessica: are trying to predict is the price of the house.

46
00:10:22.340 --> 00:10:22.845
Jessica: Okay?

47
00:10:23.810 --> 00:10:28.470
Jessica: And the input or the dependent variables

48
00:10:28.520 --> 00:10:32.819
Jessica: are the living area and the number of bedrooms.

49
00:10:33.320 --> 00:10:36.669
Jessica: Now, the one of the challenges

50
00:10:37.130 --> 00:10:56.820
Jessica: with linear regression and really, with any machine learning algorithm out there is that often you are presented with a data frame that has always only one output variable and a variable number of input variables or of columns that could be considered as input

51
00:10:57.050 --> 00:10:58.523
Jessica: so the

52
00:10:59.680 --> 00:11:03.279
Jessica: it's often the case where you have to decide

53
00:11:03.820 --> 00:11:08.469
Jessica: how many columns and which ones you should pick

54
00:11:08.510 --> 00:11:11.870
Jessica: in order to make your predictions. Okay.

55
00:11:13.090 --> 00:11:16.730
Jessica: if you use only one column

56
00:11:16.760 --> 00:11:19.230
Jessica: to predict your output.

57
00:11:19.270 --> 00:11:20.410
Jessica: You

58
00:11:21.155 --> 00:11:31.429
Jessica: you are using single linear regression. Okay? If you use more than one column, then you use multiple linear regression. That is essentially the only difference.

59
00:11:31.970 --> 00:11:37.520
Jessica: So if I were to predict the price of a house based on just the living area.

60
00:11:37.790 --> 00:11:47.650
Jessica: I would use a simple linear regression algorithm, because I'm using only one input X only one column to predict the price y.

61
00:11:48.060 --> 00:11:55.150
Jessica: if I'm using more than one. So the living area and the number of bedrooms to make the prediction

62
00:11:55.770 --> 00:12:00.479
Jessica: that that becomes a multiple linear regression problem. Okay.

63
00:12:00.480 --> 00:12:28.280
Jessica: there is going to be a lot of consideration that we're going to do a little bit today and a lot more later in the course about how many variables you choose and which variables you should choose. Okay. But why don't we start with the 1st example here, which is very simple. But I'm hoping it can give you an idea of how linear regression works.

64
00:12:30.960 --> 00:12:31.860
Jessica: Okay?

65
00:12:31.990 --> 00:12:37.690
Jessica: So here in this code cell, I am importing some libraries. So

66
00:12:37.690 --> 00:13:02.659
Jessica: nothing out of the ordinary. We also import Sklearn. I haven't told you anything about Sklearn yet, but I'm sure that whoever held the office hour last week introduced this library to you. Scikit-learn is the number one library for machine learning in Python. Every algorithm is coded used in machine in

67
00:13:02.660 --> 00:13:03.930
Jessica: sk, learn

68
00:13:04.596 --> 00:13:16.679
Jessica: it is extremely well written, extremely well known, extremely well maintained. And I, we are going to be using this library essentially until the end of the course. Okay.

69
00:13:16.800 --> 00:13:23.689
Jessica: so from this library, I am importing the linear regression algorithm that we will be using.

70
00:13:24.130 --> 00:13:32.490
Jessica: I also import, and it also imports some functions to prepare my data and to calculate the error right?

71
00:13:33.854 --> 00:13:41.280
Jessica: Now, as a 1st example, I am considering a data set that is extremely simple.

72
00:13:41.520 --> 00:13:48.760
Jessica: So this score dot Csv file has only 2 columns.

73
00:13:48.940 --> 00:13:50.639
Jessica: The hours

74
00:13:50.790 --> 00:13:55.409
Jessica: that a student has spent studying for an exam

75
00:13:55.690 --> 00:13:58.909
Jessica: and the grade that

76
00:13:59.040 --> 00:14:00.989
Jessica: the student received.

77
00:14:01.020 --> 00:14:05.770
Jessica: Okay, so the goal here is to

78
00:14:06.110 --> 00:14:09.350
Jessica: try and understand

79
00:14:09.960 --> 00:14:11.000
Jessica: what

80
00:14:11.260 --> 00:14:18.780
Jessica: is what our grade is going to be if we study a certain amount of hours. Okay?

81
00:14:19.440 --> 00:14:44.869
Jessica: So every time you have a data frame, and you know, you're gonna have a, you're gonna have to use a regression problem or any machine learning algorithm in general. One of the 1st thing that you want to ask yourself is, what is your output variable. And what are the variables that you want to use to make the prediction? Okay.

82
00:14:45.180 --> 00:14:56.820
Jessica: in some cases it can be a little bit what's the word? Ambiguous? Okay or like, the argument could go 2 way.

83
00:14:56.850 --> 00:15:12.769
Jessica: How many hours should you study to wanna to get certain score? And if you want to score, if you want your score like you can, you can flip in some situation. Essentially, you can flip the question. Okay? But in this case we're gonna use score

84
00:15:13.270 --> 00:15:17.790
Jessica: as the output and the hours as input

85
00:15:22.013 --> 00:15:33.227
Jessica: Ravi is asking if we cannot import. Sk, learn fully. Sk, learn is a massive library. Okay?

86
00:15:33.970 --> 00:15:34.970
Jessica: it's

87
00:15:35.190 --> 00:15:57.279
Jessica: contains an insane amount of functions and algorithms. And it's really because it's divided into many sub modules. Okay, it makes a lot more sense for the syntax to import each function that you're going to need. Otherwise, if you just import

88
00:16:00.730 --> 00:16:04.610
Jessica: import, sk learn. Oh.

89
00:16:04.730 --> 00:16:12.380
Jessica: sk! Learn as I don't even know how to alias it, because nobody does it as sk. Let's pretend that

90
00:16:12.470 --> 00:16:24.259
Jessica: then, to use any functions inside it, you would have to say, model equal sk dot linear model.

91
00:16:25.630 --> 00:16:26.480
Jessica: Dot

92
00:16:26.510 --> 00:16:27.820
Jessica: linear

93
00:16:28.330 --> 00:16:54.449
Jessica: regression. And you know, like it, it would become very, very cumbersome. Okay, and very lengthy to call all the functions because they're the functions are not just under sk learn. They're all divided into modules. Okay? So it's really just best to call the individual functions, and you don't have to memorize where everything belongs.

94
00:16:54.450 --> 00:17:06.060
Jessica: You can just go to your like to the to the Sklearn documentation and say, Oh, linear regression, Sklearn.

95
00:17:06.619 --> 00:17:15.779
Jessica: And it's gonna tell you exactly where the function is contained and how to call it and how to import it.

96
00:17:16.970 --> 00:17:24.850
Jessica: So the it's really not good practice to just import the old, the old library, just because it's so massive.

97
00:17:31.290 --> 00:17:33.522
Jessica: yeah. And of course,

98
00:17:34.650 --> 00:17:39.320
Jessica: alright. So before we do anything

99
00:17:39.712 --> 00:17:58.919
Jessica: there, it's always good practice to have a little bit of an idea of what's going on with our data frame. Okay? Obviously, this is extremely simple. Okay, there has 25 rows and 2 columns. The info functions. You know. I'm I'm just calling these the 2 you know, as

100
00:17:58.980 --> 00:18:04.869
Jessica: you know, out of, I guess. Habit mostly. It's not a very interesting data frame.

101
00:18:05.040 --> 00:18:11.680
Jessica: What it's always important to do, though, is to check for missing values. Okay.

102
00:18:12.280 --> 00:18:22.089
Jessica: if I I think I already said this when we talked about data cleaning, if there is one missing values in your data frame like an nin.

103
00:18:22.360 --> 00:18:34.630
Jessica: And you try to run a machine learning algorithm. The machine learning algorithm is just simply gonna say to you, there are missing values in our data frame. I don't know what to do with them, and it's not going to work. Okay.

104
00:18:35.118 --> 00:18:46.100
Jessica: so if you don't, at least, if you don't want to do any either type of data cleaning, at least to check that, there are no missing values. Okay.

105
00:18:46.610 --> 00:18:52.950
Jessica: there are no missing values here. So all good. We can also look at the correlation. Okay?

106
00:18:53.180 --> 00:18:57.739
Jessica: So our again, our data frame is very simple and

107
00:18:57.850 --> 00:19:08.899
Jessica: using a little bit of brain and logic. One can say, Well, the more you study, the better. Your grade is going to be okay. Meaning that this

108
00:19:08.910 --> 00:19:14.680
Jessica: logically seems to be a good candidate for a regression problem. For this reason.

109
00:19:15.559 --> 00:19:20.949
Jessica: If you add more columns. Okay, looking at the correlation

110
00:19:21.280 --> 00:19:31.529
Jessica: can help you. Sort of like. Understand? If there is a type of connection between certain variables. Okay, should you pick

111
00:19:31.690 --> 00:19:53.209
Jessica: this variable and maybe not the other one, to make your prediction, should you pick this 3 and not these 2? You know essentially what I'm saying is that if you do some exploratory data analysis, you look at the correlation. You look at the plots. You really understand what your data is trying to communicate to you before you apply the algorithm.

112
00:19:53.560 --> 00:19:56.859
Jessica: you're more likely that your algorithm is going to do better.

113
00:19:58.090 --> 00:20:07.290
Jessica: So we look at the correlation. Obviously there is a very high correlation between the hour that a student spends studying and the scores.

114
00:20:08.460 --> 00:20:09.196
Jessica: And

115
00:20:10.990 --> 00:20:12.430
Jessica: we can

116
00:20:12.560 --> 00:20:13.670
Jessica: almost

117
00:20:14.060 --> 00:20:20.160
Jessica: say that linear regression is probably a good candidate for this problem.

118
00:20:20.970 --> 00:20:25.190
Jessica: Now, linear regression works on

119
00:20:25.890 --> 00:20:28.140
Jessica: 2 condition. Okay.

120
00:20:28.490 --> 00:20:38.569
Jessica: 1st of all your data has to be numeric. Okay, this is an algorithm that if you have a categorical variable, it's not going to know what to do with it.

121
00:20:39.150 --> 00:20:46.920
Jessica: The other condition is that there has to be for linear regression to work. Well, okay.

122
00:20:47.090 --> 00:20:54.970
Jessica: there has to be some sort of linear relationship between your input variables and your output variables.

123
00:20:55.030 --> 00:21:04.660
Jessica: What do I mean by that? I mean that if you were to plot the like an input variable and the

124
00:21:04.790 --> 00:21:08.199
Jessica: output. In this case, hours and scores.

125
00:21:09.100 --> 00:21:34.490
Jessica: you should be able to trace some type of straight line that goes through the points. Okay, this is an excellent indicator that linear regression is a good candidate for your problem. Okay, it doesn't matter what the slope of the line is. Okay. If there is a line, if there's a straight line, it's a good indication.

126
00:21:34.490 --> 00:21:41.049
Jessica: If your data was doing something like this or something like

127
00:21:41.210 --> 00:21:42.670
Jessica: this, okay.

128
00:21:44.220 --> 00:21:47.530
Jessica: you could still use linear regression.

129
00:21:47.820 --> 00:21:53.339
Jessica: But the results are not going to be as good because linear regression is

130
00:21:53.690 --> 00:22:07.399
Jessica: programmed. Okay, to work on the assumption that your data there is some sort of underlying linear relationship between your data. Okay.

131
00:22:07.500 --> 00:22:21.240
Jessica: what do you do? If your data is not linear and it goes up and down like that, you can apply transformations to your data to make it look more linear. Okay? And linear regression is going to take care of that.

132
00:22:21.900 --> 00:22:22.920
Jessica: Anyways.

133
00:22:24.420 --> 00:22:29.750
Jessica: all seem to be looking good so far. Okay, so let's see if

134
00:22:31.240 --> 00:22:33.499
Jessica: how we can apply linear regression.

135
00:22:33.740 --> 00:22:41.871
Jessica: So the 1st thing to do is to decide or communicate to our code. What is the

136
00:22:43.440 --> 00:22:57.800
Jessica: input variable. And what is the output? Okay, there are different syntaxes to do that. You can use whatever you want. The input is going to be hours. So how many hours? If I'm studying

137
00:22:57.910 --> 00:23:05.619
Jessica: 5 h, what is my, what is my, what is my grade going to be if I study 7 h, what is my grade going to be okay?

138
00:23:05.830 --> 00:23:08.489
Jessica: And the output is going to be scores

139
00:23:08.900 --> 00:23:13.680
Jessica: alright. So then we check that input the input and the target are

140
00:23:15.640 --> 00:23:20.285
Jessica: you know, I've been defined correctly. Obviously, this is perfect.

141
00:23:20.780 --> 00:23:25.059
Jessica: the other thing that you always want to do

142
00:23:25.190 --> 00:23:38.990
Jessica: is divide your data set into something that is called a training set and a testing set. Okay, this is true for any machine learning algorithm out there. Okay.

143
00:23:39.320 --> 00:23:47.600
Jessica: why do you want to do that? Well, machine learning algorithms work by looking at the data that you're passing to them?

144
00:23:47.620 --> 00:23:48.135
Jessica: Okay.

145
00:23:48.900 --> 00:23:50.879
Jessica: if you were to pass

146
00:23:51.280 --> 00:23:54.990
Jessica: all of your data to a machine learning algorithm.

147
00:23:55.360 --> 00:24:00.659
Jessica: then you'd have no way of testing if your algorithm has learned correctly.

148
00:24:00.780 --> 00:24:18.019
Jessica: Okay. So by dividing the or by splitting. I guess your data into training and into testing you essentially are reserving a portion of that data to test the

149
00:24:18.460 --> 00:24:22.210
Jessica: trained machine learning algorithm, okay.

150
00:24:22.360 --> 00:24:41.560
Jessica: typically this splitting is done in a 80% and 20% split. So 80% for training and 20% for testing. Okay, depending on how big your data set is. You can change those values a little bit. But it's between the, you know, like

151
00:24:41.900 --> 00:24:44.879
Jessica: 70 to 80%

152
00:24:44.920 --> 00:24:47.700
Jessica: for training and the rest for testing.

153
00:24:47.850 --> 00:24:48.710
Jessica: Okay?

154
00:24:49.210 --> 00:24:57.800
Jessica: So the function that does this for you. It's also defined in a scale. Learn, it's called train test split.

155
00:24:57.860 --> 00:25:03.259
Jessica: So here I see that there is a chat to just give me one second and then I'll address that

156
00:25:04.348 --> 00:25:09.490
Jessica: to the train tested function. I am passing my input, my target.

157
00:25:09.580 --> 00:25:14.640
Jessica: how big? I want my test size to be. So in this case, 20% of the data

158
00:25:14.800 --> 00:25:19.372
Jessica: and the random state, the random state. Just set the

159
00:25:23.140 --> 00:25:25.769
Jessica: be a seed

160
00:25:30.870 --> 00:25:34.950
Jessica: for reproducibility. What does this mean? Well.

161
00:25:35.850 --> 00:25:39.659
Jessica: every time you run the code

162
00:25:39.890 --> 00:25:41.550
Jessica: and you

163
00:25:42.630 --> 00:25:45.550
Jessica: split your data into training and testing

164
00:25:45.720 --> 00:25:47.260
Jessica: this function.

165
00:25:48.060 --> 00:25:56.210
Jessica: samples the training set and the testing set sort of like, randomly, okay, meaning that every time you run the code

166
00:25:56.400 --> 00:26:19.770
Jessica: some rows of your data frame are gonna end up in the training set, and some rows are gonna end up in the testing set. Okay, if you want your splitting to always be exactly the same. So for the same rows to always end up for training, and the other rows to always end up for for testing you set this parameter to ensure that that happens. Okay.

167
00:26:20.590 --> 00:26:24.400
Jessica: I am going to take a look at the chat.

168
00:26:32.940 --> 00:26:36.390
Jessica: so if the data is not linear.

169
00:26:36.690 --> 00:26:38.730
Jessica: So it has. So

170
00:26:39.820 --> 00:26:52.129
Jessica: Richard is asking, how can how can we decide to make the data linear? If it's not linear? You can use transformations. There are a few ones.

171
00:26:52.823 --> 00:26:54.089
Jessica: Let's see.

172
00:27:11.250 --> 00:27:13.159
Jessica: yes. So

173
00:27:15.170 --> 00:27:26.670
Jessica: okay, so there are here some examples. So you see that you may have like a squared situation or a log situation. And this page?

174
00:27:32.878 --> 00:27:36.970
Jessica: you can essentially had

175
00:27:38.330 --> 00:27:44.134
Jessica: quadratic terms. Okay, sounds complicated. So if you're

176
00:27:46.000 --> 00:28:07.790
Jessica: data, for example, is like a parabola. So it follows like, X squared type, you would essentially add the terms to your linear regression algorithm to take that fact into consideration. Okay, I'm trying to see if I can find a

177
00:28:08.550 --> 00:28:14.039
Jessica: good link transformations in regression.

178
00:28:15.300 --> 00:28:16.820
Jessica: Oh.

179
00:28:28.750 --> 00:28:31.319
Jessica: yeah, this might be a little bit of a

180
00:28:32.460 --> 00:28:34.340
Jessica: intense read.

181
00:28:34.810 --> 00:28:39.999
Jessica: But you can. You can take a look at this if if you guys want.

182
00:28:41.710 --> 00:28:45.000
Jessica: Oh, you guys can't see safari. Oh, I'm sorry.

183
00:28:45.650 --> 00:28:48.360
Jessica: Let me share everything.

184
00:28:49.580 --> 00:28:50.360
Jessica: Okay?

185
00:28:53.270 --> 00:29:01.146
Jessica: yeah. So there are, there are a few different ways in which you can apply transformations.

186
00:29:04.980 --> 00:29:12.529
Jessica: probably this one is also pretty good. This might be a little bit. Oh, this is an r 2. You don't want that.

187
00:29:21.319 --> 00:29:27.069
Jessica: Yeah. So this is an example where you know, like you have, like a polynomial regression.

188
00:29:27.830 --> 00:29:44.019
Jessica: and it shows you like the code here. If you if you take a look, I can share this link with you. It shows you what to do with the code in order to bring it to a, to a linear regression, to a linear

189
00:29:44.120 --> 00:29:45.590
Jessica: dip dependency.

190
00:29:47.560 --> 00:29:49.310
Jessica: Okay.

191
00:29:50.200 --> 00:29:54.560
Jessica: alright. So where was I? Okay?

192
00:29:54.590 --> 00:29:56.906
Jessica: So now that we have

193
00:29:57.830 --> 00:30:18.209
Jessica: split well defined, our input, and output variable and split our data, we can implement the model. Okay? So you've seen a little bit how to use Sklearn last week, I think. The beauty about Sklearn is that really? Once you

194
00:30:18.660 --> 00:30:33.159
Jessica: understand how to call an algorithm. You understand how to call all of them okay? Because the steps are essentially the same for every algorithm. And that's why, earlier, I was saying that sk learn is written so well.

195
00:30:33.910 --> 00:30:40.269
Jessica: So the 1st thing that you have to do is instantiate the model. Essentially, you have to create this object

196
00:30:40.590 --> 00:30:49.779
Jessica: that tells your code. Well, prepare for this model to be to train. Okay, in this case, we just called linear regression.

197
00:30:50.410 --> 00:31:07.539
Jessica: The next step is to fit the model to your data. Okay? So here I do. I printed some documentation. So nothing really super useful for this example.

198
00:31:08.280 --> 00:31:14.980
Jessica: But the the 1st thing that you need to do is to train the model to the training data that we have defined earlier.

199
00:31:15.610 --> 00:31:21.063
Jessica: So you you call the function fit on the

200
00:31:22.170 --> 00:31:25.940
Jessica: model, the linear regression model that we just defined.

201
00:31:25.970 --> 00:31:34.930
Jessica: And you train it using the input, the training input and the training output or the target. Okay?

202
00:31:37.940 --> 00:31:47.500
Jessica: it's very fast. Okay, not. It's not very fast, because the data frame is small. It's always pretty fast. Okay, so don't be surprised by that.

203
00:31:48.200 --> 00:31:49.270
Jessica: Now.

204
00:31:49.580 --> 00:32:06.770
Jessica: earlier, during the office hour, I told you that the mathematical foundation of linear regression is the equation of the line. Okay, Y is our output. So the grade that we're going to get in our exam, X is the input

205
00:32:06.820 --> 00:32:12.979
Jessica: okay. So the hours that we're studying for the exam, and we have these 2 coefficients

206
00:32:13.140 --> 00:32:26.199
Jessica: that are defined by the model that we have trained. Okay, so depending on the data that we have okay, these values of the these 2 coefficients values are going to change.

207
00:32:26.470 --> 00:32:29.860
Jessica: One is the coefficient of the model.

208
00:32:29.930 --> 00:32:32.209
Jessica: which is data, data, not.

209
00:32:32.260 --> 00:32:36.480
Jessica: and the other one is the intercept, which is theta one.

210
00:32:36.790 --> 00:32:37.760
Jessica: Okay?

211
00:32:38.130 --> 00:32:46.949
Jessica: Out of curiosity. Let's take a look at these 2 values. It's 9.6 for the coefficient and 2.8 for the intercept

212
00:32:48.530 --> 00:32:49.770
Jessica: the

213
00:32:49.780 --> 00:32:53.489
Jessica: now that we have this model, we

214
00:32:53.640 --> 00:32:57.800
Jessica: can start looking at

215
00:32:59.170 --> 00:33:07.930
Jessica: how it performed. Okay, so there are a few different ways to go about this. But one thing that I like to do is first, st

216
00:33:08.420 --> 00:33:17.449
Jessica: look at the prediction of the model. Okay. So now you have this model that has learned on certain data.

217
00:33:17.470 --> 00:33:18.025
Jessica: Okay.

218
00:33:20.380 --> 00:33:26.429
Jessica: the next thing that you want to do is saying, Okay, have you learned well from this data or not really

219
00:33:26.860 --> 00:33:29.989
Jessica: one way to do that is to

220
00:33:30.050 --> 00:33:33.020
Jessica: apply the function, predict on the model

221
00:33:33.120 --> 00:33:55.659
Jessica: and use it to make predictions on the test input of my data set. So that portion of the data set of the data that my algorithm hasn't seen yet. Okay? Because it has only seen the training data.

222
00:33:55.860 --> 00:34:00.069
Jessica: Okay, so what you want to do now is to

223
00:34:03.370 --> 00:34:06.029
Jessica: use the predict function

224
00:34:06.120 --> 00:34:09.659
Jessica: to calculate the predicted. Y, okay.

225
00:34:10.880 --> 00:34:19.840
Jessica: so if I do that, so if I use the predict function on the test, input these are my prediction. Okay, so

226
00:34:20.730 --> 00:34:28.699
Jessica: this is what my model is predicting. Okay, if I study X amount of hours. I well, let's print

227
00:34:29.280 --> 00:34:31.280
Jessica: test inputs.

228
00:34:35.360 --> 00:34:36.170
Jessica: Okay?

229
00:34:36.400 --> 00:34:52.869
Jessica: So if I print, sorry if I print I am. I am jet lagged. I am in Europe right now, and I am clearly not doing well right now. If I study 8.3 h

230
00:34:53.040 --> 00:34:57.269
Jessica: I should get a grade of 80 around 83%.

231
00:34:57.600 --> 00:35:11.319
Jessica: If I study 2.5 5 h, my grade is gonna drop to 27, same thing with 2.7. If I study 6.9 h, my grade should be around 69%.

232
00:35:11.600 --> 00:35:18.490
Jessica: And if I study 59 is going to be around 59%. Okay, so this is what my algorithm predicted.

233
00:35:21.000 --> 00:35:26.139
Jessica: Let's see if we can plot some interesting plots.

234
00:35:26.931 --> 00:35:47.590
Jessica: This is the input the test input and the test prediction. Of course, there is a perfect line going through them. Okay, the reason why is because these values were predicted by the algorithm. So all the points are going to line like fall on a perfect line

235
00:35:49.720 --> 00:35:54.730
Jessica: the other thing that you can plot is see.

236
00:35:54.830 --> 00:35:56.990
Jessica: try and see how

237
00:35:57.070 --> 00:36:01.810
Jessica: well a line with this coefficient

238
00:36:02.280 --> 00:36:06.500
Jessica: lays over the model data. Okay?

239
00:36:06.700 --> 00:36:11.880
Jessica: So here in blue, I have my trainings and my training data.

240
00:36:12.170 --> 00:36:21.180
Jessica: The red line is the line of linear regression. And you can see that, you know. Obviously, it's not going through all the points, but

241
00:36:21.270 --> 00:36:29.890
Jessica: it fits along on them. Okay, a very good indicator that my my model has learned well from the data.

242
00:36:31.610 --> 00:36:40.719
Jessica: The other thing that we can do is to look at the error. Okay, so, and at the accuracy of the model.

243
00:36:40.780 --> 00:36:45.100
Jessica: So the accuracy is around 95%.

244
00:36:45.280 --> 00:36:51.850
Jessica: And the error is very low. 4.3 5. Okay? So again.

245
00:36:52.310 --> 00:36:56.359
Jessica: another indication that my model is working well.

246
00:36:57.654 --> 00:36:58.469
Jessica: Yet

247
00:36:58.520 --> 00:37:05.820
Jessica: we still haven't seen how the prediction of the model, compared to

248
00:37:05.940 --> 00:37:09.160
Jessica: the values that were actually in my data frame.

249
00:37:10.230 --> 00:37:12.850
Jessica: So this graph

250
00:37:13.040 --> 00:37:15.640
Jessica: contains in blue dot.

251
00:37:16.220 --> 00:37:17.430
Jessica: d

252
00:37:20.230 --> 00:37:21.120
Jessica: test

253
00:37:21.480 --> 00:37:36.610
Jessica: data frame that I split. Okay, so the portion of my data set of my data frame that I did not use to train my algorithm. Okay? Only 5 points because our data set was very small.

254
00:37:37.630 --> 00:37:39.160
Jessica: The red line

255
00:37:39.370 --> 00:37:56.719
Jessica: is the line of linear regression. Now, of course, the line of linear regression is not going to go through all the points. In fact, it doesn't touch any of them. But you can see that it goes through them nicely. Okay, very good. Indication that your problem that your model is working well.

256
00:38:01.510 --> 00:38:09.337
Jessica: it's also always a good idea to test the accuracy of the

257
00:38:11.230 --> 00:38:12.720
Jessica: testing set

258
00:38:13.650 --> 00:38:21.099
Jessica: over like, additionally to testing the accuracy of the training set. Okay.

259
00:38:21.240 --> 00:38:37.009
Jessica: every time you split your data frame into training and testing. You're always gonna end up with a training set and a testing set. Okay? And you can evaluate the accuracy of your algorithm on both of them.

260
00:38:37.450 --> 00:38:48.940
Jessica: We're going to talk more about this later in later modules. But you want those accuracies to be in the same range. Okay, 5 to 10% range.

261
00:38:49.200 --> 00:39:03.600
Jessica: If one, it's a lot lower than the other, it's not a good sign. Okay, I'm not going to spoil what's to come in the next modules, but very, very, very, very important, that these 2 accuracies are in the same range.

262
00:39:05.100 --> 00:39:08.830
Jessica: So let's take a look here.

263
00:39:08.900 --> 00:39:13.840
Jessica: So the accuracy of the train data was around 95%.

264
00:39:14.630 --> 00:39:18.960
Jessica: The accuracy of the test data is around

265
00:39:19.050 --> 00:39:24.769
Jessica: 96.5 97%. Either way very similar. Okay.

266
00:39:25.040 --> 00:39:27.729
Jessica: which is a very good sign.

267
00:39:30.140 --> 00:39:37.879
Jessica: so based on the accuracy that we got, which is a very high value. Okay, don't think that

268
00:39:37.940 --> 00:39:47.449
Jessica: you should always shoot for 95%, 94%. It's typically around, you know, like 75 to 85%, realistically.

269
00:39:48.008 --> 00:39:55.550
Jessica: but given the accuracy results, the low error. And the way these graphs look.

270
00:39:55.580 --> 00:39:59.949
Jessica: we can say that our model is working correctly. Okay.

271
00:40:00.070 --> 00:40:08.730
Jessica: now, how do you use this model. Okay, we have a model that has been trained. Now I am a student, and I want to know

272
00:40:08.870 --> 00:40:20.159
Jessica: how many hours, what? What my grade, what my grade is going to be. If I study, say, 3 HA day, okay, or 3.4 HA day. Okay.

273
00:40:20.890 --> 00:40:23.670
Jessica: you do so by

274
00:40:25.110 --> 00:40:28.759
Jessica: calculating the predicted value

275
00:40:28.780 --> 00:40:32.510
Jessica: for your model for the value 3.4.

276
00:40:32.650 --> 00:40:43.150
Jessica: Okay. So a student who has studied 3.5 3.4 HA day should get a grade around 35. Okay.

277
00:40:43.160 --> 00:40:46.589
Jessica: if you study 9.2 5 HA day.

278
00:40:46.850 --> 00:40:50.710
Jessica: your grade should be around 92%.

279
00:40:51.020 --> 00:40:51.890
Jessica: Okay.

280
00:40:53.230 --> 00:40:58.380
Jessica: And that is all I had for today. Do you guys have questions.

281
00:41:16.130 --> 00:41:19.030
Jessica: the 2 brackets together? Let me

282
00:41:19.700 --> 00:41:21.529
Jessica: bring up this again.

283
00:41:24.360 --> 00:41:26.920
Jessica: like in the

284
00:41:27.270 --> 00:41:28.220
Jessica: here.

285
00:41:30.030 --> 00:41:32.740
Jessica: like the the square brackets.

286
00:41:36.430 --> 00:41:41.290
Jessica: Oh, it's because it's a singular value.

287
00:41:41.410 --> 00:41:44.420
Jessica: So you.

288
00:41:44.780 --> 00:41:49.240
Jessica: So if you want to access.

289
00:41:50.040 --> 00:41:51.110
Jessica: So

290
00:41:51.320 --> 00:41:52.900
Jessica: test input

291
00:41:53.080 --> 00:41:54.840
Jessica: is a data frame.

292
00:41:55.460 --> 00:42:02.460
Jessica: Okay, it's a 2 dimensional array. Essentially, okay, meaning that the predict function is

293
00:42:02.690 --> 00:42:08.009
Jessica: programmed. Okay, to take a two-dimensional object. Okay.

294
00:42:08.520 --> 00:42:31.900
Jessica: the value 3.4 is just a number. Okay, if you were to pass the 3.4 into single brackets or single, like a simple parenthesis. To predict you would get an error, because predict is programmed to take 2 dimensional object. And so you need to use the double square bracket here in order for this function to works correctly.

295
00:42:32.636 --> 00:42:40.484
Jessica: You can also like, look it up to the on the documentation, you know. If you do,

296
00:42:42.270 --> 00:42:44.990
Jessica: linear regression

297
00:42:45.060 --> 00:42:48.020
Jessica: predict sk learn?

298
00:42:50.375 --> 00:42:52.070
Jessica: Should pop up

299
00:43:02.600 --> 00:43:03.600
Jessica: here.

300
00:43:04.122 --> 00:43:11.189
Jessica: It's an array like our sparse matrix. So it needs to be like, 2 dimensional quantity. Yeah.

301
00:43:11.190 --> 00:43:16.580
Raghavan Srinivasan: You. Yeah. You see now how much pain I go through with this team.

302
00:43:19.450 --> 00:43:23.070
Jessica: I don't think somebody somebody is not on mute, but they mean to be.

303
00:43:25.330 --> 00:43:28.939
Jessica: I am gonna mute. Them. I don't think that was a question for us.

304
00:43:36.480 --> 00:43:47.443
Jessica: okay, any other question or concern. I know that we are still at the beginning of the course. So you know, like these

305
00:43:50.160 --> 00:44:01.850
Jessica: 1st examples of machine learning may be confusing, but I promise you everything is gonna start making sense really quick. But yeah, Lin, yes, Poja, I think.

306
00:44:01.850 --> 00:44:31.469
Pooja: Yeah. Hi, hi, Jessica, pooja! Here I have a question like in order to. If if we want to have some detailed discussion while we are going through the certain module or certain topics, like as we started with the algorithm, and certain questions come or thoughts come in terms of comparison, the assignment that we are doing, or also something which is related to the day to day, things that we experience in the job which we need to.

307
00:44:31.470 --> 00:44:34.118
Pooja: where? Where I would like to have a

308
00:44:34.450 --> 00:44:40.869
Pooja: insights from you. So what is the best way to connect you during the course or.

309
00:44:41.490 --> 00:44:43.349
Jessica: Probably via ticket.

310
00:44:43.470 --> 00:44:44.200
Jessica: So.

311
00:44:44.200 --> 00:44:44.730
Pooja: Okay.

312
00:44:44.730 --> 00:44:48.359
Jessica: Yeah. So you you know how to open one. Right?

313
00:44:48.760 --> 00:44:49.490
Pooja: Yeah.

314
00:44:49.490 --> 00:44:50.475
Jessica: Yeah.

315
00:44:51.580 --> 00:45:03.449
Jessica: I mean, yeah. Canvas and tickets. Tickets is definitely the best way don't use. Don't use the inbox. We're not allowed to like open that. But if you go.

316
00:45:05.570 --> 00:45:08.160
Jessica: the support tab.

317
00:45:08.720 --> 00:45:10.679
Jessica: So you go here

318
00:45:11.640 --> 00:45:14.779
Jessica: and you go

319
00:45:15.190 --> 00:45:17.169
Jessica: submit a request.

320
00:45:18.280 --> 00:45:23.934
Jessica: and then you this form. Then I will get an email with your

321
00:45:25.110 --> 00:45:28.669
Jessica: sorry with your message, and I will reply, there.

322
00:45:29.330 --> 00:45:32.099
Pooja: Okay, okay. Thanks. Thanks. Jessica.

323
00:45:32.490 --> 00:45:33.690
Jessica: Yeah, no worries.

324
00:45:34.462 --> 00:45:36.590
Jessica: Yeah. Okay. So I.

325
00:45:36.590 --> 00:45:50.590
Pooja: And and sorry one. Another question that I have is like in the last module we, we had to say, share the the drop problem statement for our capstone project. Right?

326
00:45:50.590 --> 00:45:50.930
Jessica: Yeah.

327
00:45:51.347 --> 00:46:12.210
Pooja: Because I have. I need some extension in the assignment, so I would be submitting it a few days later. Now I know that when we submit the assignment after some time we cannot. There will be no comments on the assignment right? Only the grading will be available.

328
00:46:12.210 --> 00:46:12.890
Jessica: He loves.

329
00:46:12.890 --> 00:46:24.160
Pooja: Considering that that module is a problem statement and has a some kind of inference to the actual capstone project that we are going to do later in the future.

330
00:46:24.160 --> 00:46:24.719
Jessica: Yeah, yeah.

331
00:46:24.720 --> 00:46:34.149
Pooja: Is it fine? If I can raise the ticket and ask some feedback or some insight from you on the problem statement later.

332
00:46:34.150 --> 00:46:45.644
Jessica: Absolutely. And also you know, like, that is absolutely it's fine. But also there is going to be like after module 10, you guys

333
00:46:46.070 --> 00:47:11.040
Jessica: should be able like are going to be able to book like each of you, a 1-on-one consultation with your corresponding learning facilitator. So each of you is gonna have half an hour with me, or you know Ali, or whoever and we can spend that time to talk about your problem statement, your ideas for the Capstone project. So there is. There is going to

334
00:47:11.040 --> 00:47:18.599
Jessica: be time to really talk, one on one for each of you for for the Capstone project. It's just later in the course.

335
00:47:19.150 --> 00:47:20.550
Pooja: Okay. Okay. Thank you. Thank you.

336
00:47:20.550 --> 00:47:30.260
Jessica: But but yeah, if you want, if you want more feedback you know. And you don't want to wait. You can. You can definitely open a ticket, and I will reply, there.

337
00:47:30.500 --> 00:47:42.289
Pooja: Yeah, like I, if regarding the problem statement, if we came, I come across my some ideas which I want to share before defining the problem statement. So that would be fine. Right? I mean getting.

338
00:47:42.290 --> 00:47:45.350
Jessica: Yeah, yeah, no, it's okay. Yeah, yeah, it's it's fine.

339
00:47:45.430 --> 00:47:54.239
Jessica: And I don't grade the problem statements. So you know, like, I. But I'm happy to take a look and give you some feedback about what I think.

340
00:47:54.830 --> 00:47:56.900
Pooja: Okay. Okay, thank you. Thanks a lot.

341
00:47:56.900 --> 00:47:57.740
Jessica: No worries

342
00:47:59.473 --> 00:48:01.160
Jessica: anything else

343
00:48:01.280 --> 00:48:03.350
Jessica: any other question.

344
00:48:04.220 --> 00:48:07.119
Jessica: We do have some time. So I don't mind.

345
00:48:09.290 --> 00:48:22.750
Jessica: also. Yeah, I did mention that I am in Europe. So I I have moved. Okay, I have moved from Canada to Europe permanently. So you know.

346
00:48:22.920 --> 00:48:31.586
Jessica: just for like answering tickets like the office hours are not going to change. Everything stays the same. But for answering tickets

347
00:48:33.499 --> 00:48:56.519
Jessica: for answering tickets. Keep that in mind that I'm you know, a little a few hours ahead of, ahead or behind you depends on where you are. I am currently in Italy, and I will be moving to Spain. At the beginning of 2025. Yes, it's a very exciting and very happy and very a move that has been coming for a for a long while, but

348
00:48:56.630 --> 00:49:01.790
Jessica: I moved on Monday. So I'm definitely, you know, a little bit. Jet lagged still.

349
00:49:02.498 --> 00:49:20.630
Jessica: But yeah, nothing is going to change in for office hours, or for I will still be your learning. Facilitator. It's it's still me. But my, my working hours have changed. So there is that to like that to keep in mind. If in case you wait a little bit extra for tickets sometimes.

350
00:49:21.430 --> 00:49:21.940
Jessica: Okay.

351
00:49:21.940 --> 00:49:24.700
Vijay Chaganti: Hi, this is Vijay. I have a quick question.

352
00:49:26.299 --> 00:49:41.119
Vijay Chaganti: I want to use my learning at my work environment where I need to. You know. Read the system log example. Say, I have a router, and I get this log from the router right?

353
00:49:42.037 --> 00:49:47.569
Vijay Chaganti: I need to. I need to read that log and then see if there is any missing data.

354
00:49:47.650 --> 00:49:50.556
Vijay Chaganti: or if there is any you know

355
00:49:51.030 --> 00:50:02.370
Vijay Chaganti: text, or you know, strings that appear in that data and then populate that out. What module will help. You know from this. You know, course, that that.

356
00:50:02.834 --> 00:50:11.199
Jessica: For reading logs. We don't really cover that. That would be more of like an it problem.

357
00:50:11.770 --> 00:50:12.490
Vijay Chaganti: Okay.

358
00:50:13.350 --> 00:50:14.060
Vijay Chaganti: It's.

359
00:50:14.700 --> 00:50:25.580
Jessica: Yeah, no, we don't really cover that, because we now, essentially, from now until the end of the course is just going to be like machine like straight up machine learning. And AI,

360
00:50:25.840 --> 00:50:30.679
Jessica: so like the part where we, you know, like, we, we clean the data.

361
00:50:31.190 --> 00:50:40.310
Jessica: We did some cover, like I did cover some data cleaning during the 1st office hours. So module, maybe module 3. I did something

362
00:50:41.070 --> 00:50:42.320
Vijay Chaganti: It is. It is on

363
00:50:42.440 --> 00:50:52.480
Vijay Chaganti: on numerical data, right? We were not talking about, you know, text or file file content reading files or reading text file.

364
00:50:52.480 --> 00:50:57.800
Jessica: Yeah. So you know, like, well, pandas, I mean.

365
00:50:58.530 --> 00:50:59.050
Jessica: okay.

366
00:50:59.930 --> 00:51:06.790
Jessica: if your data is stored as a in a format that can be a data frame.

367
00:51:07.360 --> 00:51:17.150
Jessica: Okay? Then you can probably open that log using pandas into a data frame. Okay? Pandas does have.

368
00:51:17.630 --> 00:51:19.969
Vijay Chaganti: If if I have the data in Json format, I.

369
00:51:19.970 --> 00:51:21.460
Jessica: Oh, yeah. Yeah. Oh, yeah. Yeah.

370
00:51:21.880 --> 00:51:23.189
Jessica: Yeah, input

371
00:51:23.500 --> 00:51:25.300
Jessica: output panthers.

372
00:51:27.176 --> 00:51:29.070
Jessica: There is.

373
00:51:29.540 --> 00:51:32.249
Jessica: I'm gonna send this to the chat as well.

374
00:51:33.350 --> 00:51:37.010
Jessica: There is a lot of options.

375
00:51:37.040 --> 00:51:46.399
Jessica: Basically. Pan pandas can read any file extension you want. So Json, HTML xml. Latex.

376
00:51:46.400 --> 00:51:47.290
Vijay Chaganti: Okay.

377
00:51:47.290 --> 00:51:49.390
Jessica: Provided that

378
00:51:50.010 --> 00:51:53.000
Jessica: the the content of that file

379
00:51:53.230 --> 00:52:04.899
Jessica: can be you know, written as a data frame, right? Like, if it's just plain text you're gonna need columns and index and all that.

380
00:52:04.900 --> 00:52:06.489
Vijay Chaganti: It should be a structured data.

381
00:52:06.490 --> 00:52:07.900
Jessica: It should be structured. Yes.

382
00:52:08.230 --> 00:52:09.070
Vijay Chaganti: Okay.

383
00:52:09.150 --> 00:52:20.209
Jessica: But you, you know, like, look at the extension of your file, and most likely there is something that you know like, if it's structured pandas is going to be able to read it into a.

384
00:52:20.210 --> 00:52:31.440
Vijay Chaganti: We're going to cover processing this, this structured data like how we covered numerical data, how to clean up the cells and all how to fill the cells of you know how to.

385
00:52:31.717 --> 00:52:39.219
Jessica: I mean, I did do. I did do some data cleaning in Module 3 during my office hours, so I don't know if you were there.

386
00:52:39.220 --> 00:52:40.430
Vijay Chaganti: Yeah, yeah, I was there.

387
00:52:40.430 --> 00:52:41.365
Jessica: Yeah,

388
00:52:42.330 --> 00:52:51.599
Jessica: there is no more data cleaning done like, there isn't a module about data cleaning. What do I let me check the

389
00:52:52.740 --> 00:52:54.590
Jessica: you know what I can do.

390
00:52:55.060 --> 00:53:00.089
Jessica: The I can make a note for myself about this. I.

391
00:53:00.090 --> 00:53:04.639
Vijay Chaganti: Any links or any any any documents that I can refer. So.

392
00:53:05.353 --> 00:53:08.919
Jessica: Yeah, I mean data cleaning.

393
00:53:10.753 --> 00:53:16.669
Jessica: I mean, I think that maybe what's best for you is here.

394
00:53:16.790 --> 00:53:21.819
Jessica: I just googled data cleaning pandas. There is a million links.

395
00:53:22.320 --> 00:53:27.347
Jessica: probably depending on like what you need. You know. Exactly.

396
00:53:28.030 --> 00:53:38.569
Jessica: you know, like, maybe do some research depending on exactly what you need, but if you, you know, like, if you have any questions, you can also open a ticket. And you know, like

397
00:53:39.029 --> 00:53:47.019
Jessica: I don't know if you're in my section. But whatever whoever whoever it is that we're gonna be able to to help you for sure.

398
00:53:47.160 --> 00:53:48.790
Vijay Chaganti: Sure, sure, thank you.

399
00:53:49.418 --> 00:53:59.529
Jessica: I was gonna say something else, but I slipped my mind. Oh, I was gonna say, I should have let me look at my calendar.

400
00:54:00.780 --> 00:54:10.860
Jessica: I should have okay. The module 11 office hour module 11 is the. There is a practical application assignment. So the office hour is.

401
00:54:11.030 --> 00:54:34.040
Jessica: you know, empty because there isn't much to say. Maybe I can do that office hour on a data cleaning. I can take advantage of that break from learning. We're gonna talk a little bit about the practical application. And then I can use the rest of the time to do data cleaning. I'll make a note about that for myself, so that you guys can have an example.

402
00:54:34.040 --> 00:54:35.329
Vijay Chaganti: What what day is that.

403
00:54:35.530 --> 00:54:40.050
Jessica: That is going to be on November 14.th

404
00:54:40.570 --> 00:54:41.570
Vijay Chaganti: Thank you. Yeah.

405
00:54:41.790 --> 00:54:43.480
Jessica: I'll make a note about that.

406
00:54:43.990 --> 00:54:44.980
Jessica: Okay.

407
00:54:46.620 --> 00:54:52.690
Jessica: Alright. Yeah. I guess that is all for today.

408
00:54:53.600 --> 00:54:55.450
Jessica: Yes, okay.

409
00:54:55.630 --> 00:55:13.059
Jessica: all right, guys, thank you so much for coming. I hope that you found today's lesson or office hour. I guess. Useful. Keep practicing with linear regression. It's fun. I will be sharing the material. There is also a little bit of another exercise below

410
00:55:13.510 --> 00:55:27.230
Jessica: for you to, you know. Like, challenge yourself a little bit if you want. But yeah, if good luck with Module 7, and I will see you in a couple of weeks, bye, and have a good rest of your day.
