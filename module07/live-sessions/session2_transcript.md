WEBVTT

1
00:00:00.290 --> 00:00:00.990
Vikesh K: Okay.

2
00:00:01.140 --> 00:00:14.019
Vikesh K: none of you are switched on your cameras. If I it would be nice to see people if you can. That would be lovely. I've also shared one Jupiter notebook and again, if people join, if you can share that with them that would be helpful.

3
00:00:14.200 --> 00:00:16.509
Vikesh K: I would share my screen.

4
00:00:17.060 --> 00:00:19.430
Vikesh K: Let me know when you can see that.

5
00:00:20.400 --> 00:00:21.140
Vikesh K: Okay?

6
00:00:21.340 --> 00:00:23.050
Vikesh K: And.

7
00:00:24.330 --> 00:00:25.740
Vikesh K: by the way, just one.

8
00:00:25.770 --> 00:00:37.089
Vikesh K: Okay, I will talk about these things later. Let's see. Okay, I can see. See avinash avinash. Hi! Good to see you. I only see avinash for the timing. Now, Sashi. Hello, Hi! Good to see you.

9
00:00:38.080 --> 00:00:39.769
Vikesh K: Okay. So

10
00:00:40.130 --> 00:00:45.990
Vikesh K: we are live and recording, and maybe couple of people more, more people will join.

11
00:00:46.130 --> 00:00:51.680
Vikesh K: So can we have Jintan, Mike, Shikar, Vijay Vikash lovely.

12
00:00:52.690 --> 00:00:53.600
Vikesh K: So

13
00:00:54.290 --> 00:01:11.210
Vikesh K: now we enter into the machine learning part. I think you already started last week. Unsupervised week. Unsupervised learning was the last week content. This week we start with one of the basics, which is linear regression. I won't really go through the theory, because I presume you have gone through the theory.

14
00:01:11.390 --> 00:01:26.959
Vikesh K: But one of the simple thing you have to admit you have to remember is linear regression is just a weighted average of different coefficients. So let's say, if I say something is, you know you use a coefficient, and I use alpha.

15
00:01:27.070 --> 00:01:31.020
Vikesh K: Then it would be beta one plus, let's say, element one.

16
00:01:31.340 --> 00:01:34.480
Vikesh K: Sorry I'm using mouse. So this looks very bad.

17
00:01:34.930 --> 00:01:42.829
Vikesh K: Beta. 2. Then you have X 2. Okay, let's say, this is your price. This is your advertisement, all right.

18
00:01:42.880 --> 00:01:47.169
Vikesh K: And this is your sales. Okay? So as a company. You want to figure out the sales.

19
00:01:47.520 --> 00:01:48.550
Vikesh K: and you

20
00:01:48.880 --> 00:01:51.820
Vikesh K: think it's dependent on price, which is x 1,

21
00:01:52.400 --> 00:01:56.010
Vikesh K: or you can call it p. 1, or it's dependent on

22
00:01:56.150 --> 00:02:00.820
Vikesh K: advertisement, these 2 parameters. But how do they connect with each other?

23
00:02:01.150 --> 00:02:04.300
Vikesh K: That's what these coefficients will tell you.

24
00:02:04.850 --> 00:02:17.060
Vikesh K: So. Coefficients, if you plug in the number. It's simple arithmetic. You need to figure out this part, then you put in the Beta one number beta 2 number, which is which the linear regression method will allow you to figure out how to do that.

25
00:02:17.200 --> 00:02:19.790
Vikesh K: And once you figure out that part

26
00:02:20.610 --> 00:02:32.959
Vikesh K: this as a business person, you know the price advertisement you can set. So you plug in the numbers, and you will get your desired sales, or at least the expected sales, which is there. All right? So this is one of the very simple method

27
00:02:33.180 --> 00:02:35.610
Vikesh K: by which you can figure out

28
00:02:35.920 --> 00:02:37.789
Vikesh K: what happens in the background.

29
00:02:38.170 --> 00:02:38.920
Vikesh K: All right.

30
00:02:39.070 --> 00:02:40.070
Vikesh K: So

31
00:02:40.360 --> 00:02:48.909
Vikesh K: there are a couple of other things which usually I talk about. But I think we won't have a lot of time, so I will talk about it later towards the end if we get time.

32
00:02:49.228 --> 00:02:55.350
Vikesh K: Remind me. But right now I want to get started with a case study. So I've shared a case study with all of you. I will reshare it.

33
00:02:55.931 --> 00:02:58.398
Vikesh K: You can. You can follow along.

34
00:02:59.570 --> 00:03:03.660
Vikesh K: this is about car prices. Okay?

35
00:03:03.720 --> 00:03:19.909
Vikesh K: If some of you are trying to planning to buy a car. So especially if you buy planning to buy a secondhand car. This is one of the most quantitative way you can approach this problem, and then you can apply the same principles, for let's say you want to buy a house. What should be the ideal house

36
00:03:19.950 --> 00:03:25.780
Vikesh K: price. So 1st we load all the modules, then we import the data set.

37
00:03:26.270 --> 00:03:27.720
Vikesh K: And if you see

38
00:03:27.790 --> 00:03:30.389
Vikesh K: the data set is 11,000 entries

39
00:03:30.690 --> 00:03:37.059
Vikesh K: alright, and you have 15 columns. And this is how the different columns look like you have bunch of

40
00:03:37.480 --> 00:03:46.000
Vikesh K: categorical data, and you have integer data. All right. I just create an original copy of it. I will show you how the data set looks like.

41
00:03:46.500 --> 00:03:48.610
Vikesh K: By the way, we often use head.

42
00:03:48.630 --> 00:04:03.500
Vikesh K: It's better to use sample rather than head, because you get values randomly picked up. So you can see a better. You know a better distribution variation in the data. So you have. What you have is the make. Who's the manufacturer? The model number

43
00:04:03.640 --> 00:04:06.039
Vikesh K: your engine fuel type

44
00:04:06.725 --> 00:04:09.800
Vikesh K: engine horsepower engine cylinders transmission

45
00:04:10.545 --> 00:04:15.599
Vikesh K: driven vehicle. What kind of vehicle it is? Front wheel driven number of droves market category

46
00:04:15.730 --> 00:04:23.809
Vikesh K: vehicle size. We could style highway miles per gallon city, miles per Gallon and Msrp. This is what you're trying to figure out. You know.

47
00:04:23.860 --> 00:04:31.399
Vikesh K: you want to understand what would be the selling price of this car? You have categorical and you have numerical variables.

48
00:04:32.140 --> 00:04:35.219
Vikesh K: Is the problem statement clear what you have to do

49
00:04:36.610 --> 00:04:37.310
Vikesh K: right?

50
00:04:37.570 --> 00:04:38.440
Vikesh K: So

51
00:04:38.570 --> 00:04:42.830
Vikesh K: we will do step by step. There are a couple of things you would go through.

52
00:04:43.140 --> 00:04:46.840
Vikesh K: 1st is, how do we treat the categorical data.

53
00:04:47.590 --> 00:04:48.970
Vikesh K: Any clue on that.

54
00:04:54.730 --> 00:04:55.809
Ravi: One hot.

55
00:04:56.160 --> 00:04:57.135
Vijay Chaganti: Yeah. One hot

56
00:04:58.380 --> 00:05:00.130
Vikesh K: Okay. One hot encoding.

57
00:05:00.130 --> 00:05:01.400
Ravi: Yeah, encoding it.

58
00:05:02.098 --> 00:05:04.730
Vikesh K: Can someone tell me, what does that do.

59
00:05:06.240 --> 00:05:07.213
Ravi: Basically it

60
00:05:07.820 --> 00:05:09.510
Ravi: expands the

61
00:05:09.570 --> 00:05:12.519
Ravi: the unique values as columns.

62
00:05:12.890 --> 00:05:13.640
Vikesh K: Okay. Cool.

63
00:05:13.640 --> 00:05:14.020
Ravi: Do that.

64
00:05:14.020 --> 00:05:14.680
Vikesh K: And

65
00:05:15.440 --> 00:05:18.970
Vikesh K: and so is this the only way? Can we do something else?

66
00:05:20.750 --> 00:05:23.900
Vikesh K: Can I can I, for example, let's say, if I have to translate this.

67
00:05:24.550 --> 00:05:27.600
Vijay Chaganti: Can you have multiple models for each variable.

68
00:05:29.265 --> 00:05:31.640
Vikesh K: Think you were saying, or avinash.

69
00:05:31.640 --> 00:05:35.360
Vijay Chaganti: Do doing multiple models for each category.

70
00:05:35.910 --> 00:05:39.319
Vikesh K: Multiple models for each category. What do you mean?

71
00:05:45.330 --> 00:05:58.850
Avinash Gangwal: 2 things we can either divide. Let's say, transmission type. There are only 2 possible values, manual and automatic, right? So we can divide the set, like one, is based on manual.

72
00:05:59.080 --> 00:06:04.460
Avinash Gangwal: What is the prediction and what is based on automatic? What is the prediction?

73
00:06:04.760 --> 00:06:06.699
Avinash Gangwal: That's 1 way of doing it?

74
00:06:07.640 --> 00:06:15.950
Avinash Gangwal: And another way is we can set the value. But that's not right. That's what the video says that we can set the value one

75
00:06:16.080 --> 00:06:17.280
Avinash Gangwal: 0

76
00:06:17.470 --> 00:06:22.999
Avinash Gangwal: and make that as an integer column and run the regression on it.

77
00:06:23.770 --> 00:06:25.599
Vikesh K: Okay, okay, cool. Good point.

78
00:06:26.325 --> 00:06:27.069
Vikesh K: What do you break?

79
00:06:27.070 --> 00:06:32.960
Vijay Chaganti: Is choose one regression model for manual and another regression model for automatic, and then

80
00:06:33.240 --> 00:06:37.540
Vijay Chaganti: met these 2 models together to get the final regression model.

81
00:06:38.010 --> 00:06:41.640
Vikesh K: See in theory you can do that, but you also lose a quite an important

82
00:06:41.950 --> 00:06:54.689
Vikesh K: set of information so ideally, if possible. If you can retain this data set structure as it is, and rather than building. So because maybe there's 1 category which has only, let's say, 5 rows right?

83
00:06:54.780 --> 00:07:02.919
Vikesh K: And it's too tiny. And then maybe you don't. You won't have enough material or enough training data to make a good model.

84
00:07:03.380 --> 00:07:13.819
Vikesh K: So in theory you can do that. But that's not the most optimal method. A, and it's a cumbersome method. Let's say you have a data categorical data which has 5 sub entries or 6 sub entries.

85
00:07:14.440 --> 00:07:23.290
Vikesh K: If you start making 6 models for act it can quite painfully, all right. The second thing which one of the point was raised around label encoding.

86
00:07:23.490 --> 00:07:25.979
Vikesh K: And I want to show you the

87
00:07:29.800 --> 00:07:34.814
Vikesh K: the psychic documentation for that, because it's important as you now go through

88
00:07:35.320 --> 00:07:46.410
Vikesh K: machine learning, if possible, whatever technique you could use, at least go through documentation. Once go through the documentation that's helpful. They also give you some examples. So it it allows you to make a good idea.

89
00:07:46.820 --> 00:07:49.300
Vikesh K: Now, one thing you should, you would see.

90
00:07:49.310 --> 00:07:54.330
Vikesh K: this transformer should be used to encode target values, that is y and not the input.

91
00:07:54.340 --> 00:07:58.769
Vikesh K: So never, ever use label encoder with X values

92
00:07:59.090 --> 00:08:04.280
Vikesh K: only always with y values. Y values means what you wish to predict.

93
00:08:04.880 --> 00:08:09.590
Vikesh K: Okay, that should be labeled encoded as 1, 2, 3, 4. That's fine

94
00:08:10.608 --> 00:08:17.939
Vikesh K: but never with input X, because the problem there is, let's say, I have

95
00:08:18.050 --> 00:08:19.599
Vikesh K: 3 vehicle sizes.

96
00:08:19.680 --> 00:08:23.740
Vikesh K: No, not this one. This is not a good idea. Let's say I have a vehicle style. Okay.

97
00:08:23.840 --> 00:08:35.330
Vikesh K: let's say I will make this as one. This is 2, this is 3. This is 4. Then Sedan is again one. Sedan is again one, then coupe is 4. Okay, so

98
00:08:37.510 --> 00:08:43.820
Vikesh K: in general there is no hierarchy between these categorical values. Or let's say, maybe this is some

99
00:08:44.211 --> 00:08:50.310
Vikesh K: location. But when I put it 1, 2, 3, 4, I'm creating a hierarchy there. I'm creating a structure

100
00:08:50.840 --> 00:08:54.259
Vikesh K: which is not there in the original data set. So it's wrong.

101
00:08:54.510 --> 00:08:59.369
Vikesh K: So don't do label encoding with your categorical with your X values.

102
00:08:59.640 --> 00:09:03.460
Vikesh K: the values which you are going to use to predict something.

103
00:09:03.490 --> 00:09:05.159
Vikesh K: So I'm going to use

104
00:09:05.240 --> 00:09:08.850
Vikesh K: all these values to predict Msrp.

105
00:09:08.920 --> 00:09:12.550
Vikesh K: so when I have all these values I should never, ever

106
00:09:12.580 --> 00:09:14.160
Vikesh K: do this label encoding.

107
00:09:14.560 --> 00:09:17.750
Vikesh K: Okay, best method is one hot encoding.

108
00:09:17.990 --> 00:09:22.199
Vikesh K: There's also something called ordinal encoding. We will maybe talk about it later.

109
00:09:22.536 --> 00:09:26.549
Vikesh K: There are cases where you can maybe put some structure. But one hot encoding

110
00:09:26.560 --> 00:09:28.560
Vikesh K: is more or less the safe bet.

111
00:09:29.390 --> 00:09:30.120
Vikesh K: Okay.

112
00:09:32.010 --> 00:09:35.399
Vikesh K: yes, like, Shashi said, all input should have equal standing.

113
00:09:35.610 --> 00:09:36.630
Vikesh K: Now, one.

114
00:09:36.840 --> 00:09:42.129
Vikesh K: So one problem where one hot encoding can be problematic is when you have too many categories.

115
00:09:42.350 --> 00:09:45.150
Vikesh K: So, for example in this. If you see model.

116
00:09:45.200 --> 00:09:49.299
Vikesh K: I believe you have too many models. So if you make one hot encoding.

117
00:09:49.320 --> 00:09:56.220
Vikesh K: maybe you will add 50 more columns to your data set, and that can be quite painful. And it adds a lot of noise to the data.

118
00:09:56.650 --> 00:09:57.400
Vikesh K: Okay.

119
00:09:57.902 --> 00:10:02.360
Vikesh K: we will. We will talk about it later. But this is these are the points I want you to remember.

120
00:10:02.910 --> 00:10:05.869
Vikesh K: So what the safe bet is one hot encoding?

121
00:10:06.710 --> 00:10:07.520
Vikesh K: All right.

122
00:10:09.780 --> 00:10:15.369
Vikesh K: That's the main thing. I will, I will 1st what I will do. We will 1st focus on the numerical columns.

123
00:10:15.540 --> 00:10:19.739
Vikesh K: create that user model, go through the process end to end.

124
00:10:19.860 --> 00:10:21.830
Vikesh K: and then we will go

125
00:10:21.960 --> 00:10:23.590
Vikesh K: for the categorical data.

126
00:10:23.830 --> 00:10:24.610
Vikesh K: Alright

127
00:10:25.420 --> 00:10:31.750
Vikesh K: do it combined. So now, if you see the column names, I will show you the column names. Df, dot columns.

128
00:10:32.520 --> 00:10:41.879
Vikesh K: it's not in the proper format. So, for example, you will see there is a space right? So if I'm trying to type, write down these names.

129
00:10:41.960 --> 00:10:49.209
Vikesh K: It can be quite problematic. It can quite painful. And I can. I can go wrong right market. Then there's a space. So what I will do.

130
00:10:49.230 --> 00:10:51.440
Vikesh K: I will apply series of functions

131
00:10:51.510 --> 00:10:56.549
Vikesh K: to change to clean the column name. So 1st I I'm

132
00:10:57.220 --> 00:10:58.690
Vikesh K: doing lowercase

133
00:10:59.090 --> 00:11:04.360
Vikesh K: for all the one that's the 1st step, then the second step is, I'm stripping the white space.

134
00:11:05.950 --> 00:11:08.510
Vikesh K: the the space around

135
00:11:11.930 --> 00:11:14.730
Vikesh K: the column names. I hope this works in sequence.

136
00:11:15.550 --> 00:11:16.339
Vikesh K: And M,

137
00:11:16.670 --> 00:11:18.920
Vikesh K: replacing the blank space

138
00:11:21.030 --> 00:11:24.149
Vikesh K: with a semicolon with a underscore.

139
00:11:24.260 --> 00:11:32.060
Vikesh K: So once I do all these operations, you will see my column names look slightly better. Okay, there's a lesser chance to make mistakes.

140
00:11:32.110 --> 00:11:39.890
Vikesh K: So vehicle size this is with a space. Now, this is underscore there. So it's also easy to type, and there's a less chances that I will make mistake.

141
00:11:40.200 --> 00:11:44.710
Vikesh K: Okay? So sometimes you might have to do these consistency things. Just be careful about it.

142
00:11:45.010 --> 00:11:51.839
Vikesh K: Then the duplicated check important. There are 700 to 15 duplicates. What should we do regarding the duplicates.

143
00:11:53.470 --> 00:11:55.430
Avinash Gangwal: Drop drop them.

144
00:11:55.750 --> 00:11:57.810
Vikesh K: Would that affect the model quality.

145
00:12:00.340 --> 00:12:05.570
Avinash Gangwal: Not really because it's duplicate data, right? Exact duplicate data.

146
00:12:05.810 --> 00:12:18.779
Vikesh K: Yeah, essentially, it's the same information being repeated. So it it won't make any impact to the model. Essentially, you should drop it. Also, let's say sometimes you have might have a lot of duplicates. It will also reduce the computation type.

147
00:12:20.560 --> 00:12:24.799
Vikesh K: So I will duplicate deduplicate the data set.

148
00:12:24.830 --> 00:12:28.910
Vikesh K: And then this is my new shape. Alright, and I can again check.

149
00:12:30.260 --> 00:12:33.190
Vikesh K: I don't have any duplicates now. Missing values.

150
00:12:34.199 --> 00:12:42.940
Vikesh K: There are some missing values here, right? But remember what I said previously, also, missing values should always be seen in the context.

151
00:12:43.400 --> 00:12:46.990
Vikesh K: You have an absolute number here. You have an absolute number here, but

152
00:12:47.310 --> 00:12:56.589
Vikesh K: it doesn't give you much information. What gives you much information if you convert this into percentages, and how do you do that is rather than using dot sum you use dot mean.

153
00:12:57.890 --> 00:13:10.059
Vikesh K: now, what I know market category is 30% missing engine horsepower is only 0 point 6 2% fuel type is 0 point 0 3% missing. And then cylinders is 0 point 2 7% missing.

154
00:13:10.250 --> 00:13:13.460
Vikesh K: I multiply it by 100. So everything is in percentages.

155
00:13:14.050 --> 00:13:17.130
Vikesh K: So this gives us some good information.

156
00:13:17.880 --> 00:13:21.189
Vikesh K: What? What would you do for the missing values?

157
00:13:21.530 --> 00:13:25.320
Vikesh K: Yeah, okay? And also, would there be a problem for the linear regression.

158
00:13:30.100 --> 00:13:43.139
Avinash Gangwal: So if mean is, the percentage is less, maybe we can drop them. But market category is something we cannot drop it. So we need to put the MoD value if it is

159
00:13:43.350 --> 00:13:45.100
Avinash Gangwal: non-integer number.

160
00:13:45.370 --> 00:13:46.010
Avinash Gangwal: cool.

161
00:13:46.010 --> 00:13:46.740
Vikesh K: Okay?

162
00:13:46.930 --> 00:13:51.859
Vikesh K: And then, what is the right step to do it? Should I do it right now?

163
00:13:52.020 --> 00:13:53.820
Vikesh K: Or should I wait it

164
00:13:56.620 --> 00:13:58.030
Vikesh K: way to do it later.

165
00:13:59.810 --> 00:14:00.730
Vikesh K: Waiting room.

166
00:14:05.110 --> 00:14:05.720
Avinash Gangwal: This.

167
00:14:06.040 --> 00:14:12.979
Avinash Gangwal: How you remove the duplicate. I see the code. It says, Df. Duplicated, not.

168
00:14:13.880 --> 00:14:15.510
Avinash Gangwal: What is it? Oh.

169
00:14:15.600 --> 00:14:18.690
Avinash Gangwal: this is a way to delete that, Tilde.

170
00:14:18.690 --> 00:14:23.700
Vikesh K: Yeah. So what I'm doing. If you do, df dot duplicated, it will tell you false and true. Right?

171
00:14:23.900 --> 00:14:29.160
Vikesh K: So how does the whole thing work if I do. Df, and then put this

172
00:14:30.320 --> 00:14:31.030
Vikesh K: ping

173
00:14:31.210 --> 00:14:39.190
Vikesh K: inside like the in the brackets. Only true true values I should be wherever you now that have removed. So I can't show you that.

174
00:14:39.300 --> 00:14:43.140
Vikesh K: But wherever they were true, that true values would have been shown to you.

175
00:14:43.570 --> 00:14:48.529
Vikesh K: And then, Tilde, what essentially Tilde does, it reverses the whole thing.

176
00:14:49.550 --> 00:14:51.030
Vikesh K: Okay? So

177
00:14:51.850 --> 00:14:57.859
Vikesh K: you have. Let me run this. So you see false, false for 0 1, 2, 3, 4. You see false.

178
00:14:58.070 --> 00:15:01.180
Vikesh K: If I take this Tilde and I put this at the start.

179
00:15:01.380 --> 00:15:03.199
Vikesh K: it will reverse the whole thing.

180
00:15:04.010 --> 00:15:07.270
Vikesh K: So what I'm saying so remember what would have happened

181
00:15:07.290 --> 00:15:11.420
Vikesh K: is when you had df dot duplicated wherever you have to.

182
00:15:11.510 --> 00:15:15.460
Vikesh K: That will become false, and then automatically, that will be dropped

183
00:15:16.820 --> 00:15:18.200
Vikesh K: from use of selection.

184
00:15:20.200 --> 00:15:30.750
Vikesh K: Just this right later on. You will, you know, maybe 1st time, if you're looking at it. This looks really complicated. But yeah, this is sort of more of a logical operation in the back end.

185
00:15:32.580 --> 00:15:33.620
Vikesh K: Make sense.

186
00:15:34.560 --> 00:15:37.260
Vikesh K: Okay. Others who are very silent

187
00:15:37.280 --> 00:15:39.209
Vikesh K: and who joined little late.

188
00:15:39.320 --> 00:15:55.660
Vikesh K: I have shared a Jupyter notebook and what we are trying to do is we have cars, data. We have data for cars, and we are trying to figure out the price of a car using different parameters that we have. And we have bunch of numerical plus categorical characters. Okay.

189
00:15:56.400 --> 00:15:57.570
Vikesh K: so

190
00:15:57.860 --> 00:16:07.439
Vikesh K: duplicate missing values. So missing values. I won't touch for the timing. It's good to know, but I won't impute that at this stage I will impute it later, and I will tell you why.

191
00:16:09.220 --> 00:16:16.670
Vikesh K: Now let's do some analysis of the Msrp column. This is what we wish to predict. So whatever column you wish to predict.

192
00:16:17.260 --> 00:16:20.910
Vikesh K: please do a thorough investigation and understanding of that column.

193
00:16:21.290 --> 00:16:22.090
Vikesh K: All right.

194
00:16:22.494 --> 00:16:31.339
Vikesh K: So 1st thing let's say you do. Df dot describe, you will see the mean price is around 41,000 or 42,000. Let's let's remember it like that.

195
00:16:31.650 --> 00:16:37.219
Vikesh K: Median is around 30,000. Max is a huge number.

196
00:16:37.530 --> 00:16:44.340
Vikesh K: and then you have 50 percentile, which is, I saw media, 75th percentile is 43,000. All right.

197
00:16:44.740 --> 00:16:53.590
Vikesh K: If I add these values, you can also see 95th percentile, 99th percentile. Right? If you add these P here, so you can

198
00:16:53.950 --> 00:16:57.390
Vikesh K: look, you can deep dive into describe and see further

199
00:16:57.450 --> 00:17:01.880
Vikesh K: at further quantizer for further percentiles. Now, we should

200
00:17:02.470 --> 00:17:10.179
Vikesh K: visualize this, you will see these are the outliers in the data set. All right. So this is a big outlier. This is the big outlier, which

201
00:17:10.630 --> 00:17:16.179
Vikesh K: is that dangerous for linear regression? Or is it fine when you have outliers.

202
00:17:17.290 --> 00:17:18.099
Avinash Gangwal: No, it's.

203
00:17:19.669 --> 00:17:20.899
Vijay Chaganti: We we should.

204
00:17:20.900 --> 00:17:21.940
Avinash Gangwal: Outline.

205
00:17:22.950 --> 00:17:26.610
Vikesh K: Okay, we should remove the yeah. So so when you have outliers, remember.

206
00:17:26.760 --> 00:17:36.590
Vikesh K: there are some algorithms, for example, decision tree, they don't really care they will work fine. But if you have algorithms like linear regression.

207
00:17:37.140 --> 00:17:44.620
Vikesh K: they have, they operate under certain assumptions, and your data should not be, should not have idly have outliers, because that will distort the whole thing.

208
00:17:45.050 --> 00:17:47.400
Vikesh K: Okay, so be be careful about that.

209
00:17:49.620 --> 00:17:52.439
Vikesh K: So we would need to focus on that.

210
00:17:52.520 --> 00:18:11.089
Vikesh K: There's another way you can look at the data which is your density plot. Again, you can see a huge spike, and there is a huge tail here, but most of the values are constituted around 1 point, and this becomes automatically. This is a bit annoying. Sometimes this converts this into scientific notation. So what you will see this is one into

211
00:18:11.310 --> 00:18:26.159
Vikesh K: 10 raised to power. 6. This is 2 into 10 raised to power. 6. Okay. Remember, when you have E, 6, that is anything raised to 10 raised to power? 6. If it's minus 6, this would be into 10 raised to power minus 6.

212
00:18:26.310 --> 00:18:28.649
Vikesh K: Okay, this will be in decimal points.

213
00:18:29.008 --> 00:18:37.640
Vikesh K: This is a little annoying. But at least you see the distribution. This happens automatically. Yeah, with some code, with some more changes, you can actually change this.

214
00:18:38.320 --> 00:18:40.149
Vikesh K: You can also look at the histogram.

215
00:18:40.580 --> 00:18:52.379
Vikesh K: but usually it's good to at least have an idea of how the density plot looks like that will give you an idea of the shape. You can also put X limits by that. You can, you know, just focus on a certain segment.

216
00:18:52.740 --> 00:18:54.729
Vikesh K: Now, one of the things you can do

217
00:18:56.270 --> 00:19:04.859
Vikesh K: because we would like the for better predictions in linear regression. One of the assumption is that the Y variable should be

218
00:19:05.465 --> 00:19:07.689
Vikesh K: should be numeric should be

219
00:19:07.760 --> 00:19:09.270
Vikesh K: normally distributed.

220
00:19:09.600 --> 00:19:17.199
Vikesh K: So one of the ways you normally distribute is by converting this into a log. Okay, so I will create one more column, which will be a log

221
00:19:17.260 --> 00:19:20.449
Vikesh K: of Msrp. And as you can see, Msrp log.

222
00:19:20.550 --> 00:19:24.349
Vikesh K: and you use that, and then, if you plot these values.

223
00:19:24.890 --> 00:19:31.599
Vikesh K: it will be slightly better in shape, and you can see there's 2 peaks. But at least this is more or less normally distributed.

224
00:19:31.730 --> 00:19:34.639
Vikesh K: and the idea being this idly should work

225
00:19:34.720 --> 00:19:36.140
Vikesh K: slightly better

226
00:19:36.420 --> 00:19:40.769
Vikesh K: when you're trying to plot it, and also you will see the change in the box plot the box plot.

227
00:19:40.870 --> 00:19:49.579
Vikesh K: Now there are outliers on both the ends. But this is how the box Ployer now looks like, so there would be tails on both the ends. But this is more or less normally distributed.

228
00:19:49.990 --> 00:19:52.289
Vikesh K: which in theory says would be a better

229
00:19:52.370 --> 00:19:58.810
Vikesh K: a way to predict the Y value. It will lead to better predictions. And we can you know everything we can embed will check.

230
00:19:59.261 --> 00:20:04.529
Vikesh K: You know, everything that you're studying. Theory, experiment. See what works and what doesn't work

231
00:20:05.020 --> 00:20:06.490
Vikesh K: making sense. So far.

232
00:20:08.000 --> 00:20:13.239
Vikesh K: Okay, I'm I'm going a little at fast pace. Certainly, because we have couple of things to cover.

233
00:20:13.360 --> 00:20:15.560
Vikesh K: Otherwise I would have liked all of you to

234
00:20:15.920 --> 00:20:18.080
Vikesh K: answer. These things make it more interactive.

235
00:20:18.340 --> 00:20:20.910
Vijay Chaganti: When you say log means, is it a logademic model?

236
00:20:21.110 --> 00:20:27.720
Vikesh K: Yes, the log. What we I will. Just take a log of natural log of this and convert this into log values.

237
00:20:28.760 --> 00:20:29.530
Vikesh K: Okay.

238
00:20:29.750 --> 00:20:37.409
Vikesh K: now outlier treatment. So remember, I talked about, there are outliers. There are 3 ways, 2 ways to do it. One is the Z score.

239
00:20:37.610 --> 00:20:39.399
Vikesh K: One is the Iqr method.

240
00:20:39.540 --> 00:20:40.310
Vikesh K: Okay?

241
00:20:41.071 --> 00:20:44.680
Vikesh K: Z, score is, if your data is normally distributed.

242
00:20:44.770 --> 00:20:53.809
Vikesh K: anything which is beyond 3 standard deviation is an outlier. So you remove anything which is 3 standard deviation here and 3 standard deviation here.

243
00:20:54.430 --> 00:20:57.580
Vikesh K: Okay, so if you remove it from both the ends

244
00:20:57.924 --> 00:21:02.959
Vikesh K: in a way of solve, solve the outlier problem. So I will. I will do the

245
00:21:03.430 --> 00:21:06.890
Vikesh K: Z Score method. So, for example, if I take this data set.

246
00:21:07.100 --> 00:21:10.960
Vikesh K: then I calculate a Z score of this column, which is Msrp.

247
00:21:11.150 --> 00:21:18.580
Vikesh K: And since I'm taking the Absolute, so anything which is greater than 3 here, you know more than negative 3

248
00:21:18.670 --> 00:21:22.610
Vikesh K: and more than positive. 3. And since I'm taking absolute.

249
00:21:22.800 --> 00:21:27.059
Vikesh K: so both the values will be converted into positive 3. So I'm removing that.

250
00:21:27.310 --> 00:21:29.500
Vikesh K: And I'm creating a new

251
00:21:30.130 --> 00:21:31.989
Vikesh K: data set. And

252
00:21:42.060 --> 00:21:45.390
Vikesh K: let me rename this. Okay, yes.

253
00:21:45.430 --> 00:21:52.400
Vikesh K: and that will. If I do that, I lose around 1.8% of the data set. So if I do, a Z score methods

254
00:21:52.560 --> 00:21:58.919
Vikesh K: from both the ends, and especially this will be from the higher end. I lose all the major outlier points

255
00:21:59.130 --> 00:21:59.870
Vikesh K: right.

256
00:22:00.020 --> 00:22:01.140
Vikesh K: and

257
00:22:02.230 --> 00:22:09.580
Vikesh K: I can check this. There would be see a few, some more outliers, but the from the original method, the outliers that we saw

258
00:22:09.980 --> 00:22:11.250
Vikesh K: that has been removed.

259
00:22:11.310 --> 00:22:15.259
Vikesh K: Alright, we can check that again via this method.

260
00:22:15.800 --> 00:22:18.300
Vikesh K: If I do. Df, dot describe

261
00:22:19.530 --> 00:22:21.760
Vikesh K: hopefully that should give us something.

262
00:22:29.250 --> 00:22:32.539
Vikesh K: 2, 2, 5, 400. What was the original one.

263
00:22:38.340 --> 00:22:39.919
Vikesh K: So this was

264
00:22:39.950 --> 00:22:41.260
Vikesh K: 2 million right?

265
00:22:41.510 --> 00:22:43.270
Vikesh K: Max was 2 million.

266
00:22:43.360 --> 00:22:45.029
Vikesh K: Now, after removing

267
00:22:46.060 --> 00:22:47.070
Vikesh K: are.

268
00:22:47.690 --> 00:22:49.450
Vikesh K: Max is

269
00:22:50.540 --> 00:22:55.670
Vikesh K: 2, 25 k, okay, so anything which is greater than 2 25 K.

270
00:22:55.690 --> 00:23:01.729
Vikesh K: Was considered an outlier that was basically beyond 3 standard deviations and has been removed.

271
00:23:02.290 --> 00:23:04.580
Vikesh K: Okay, so hopefully, now.

272
00:23:05.870 --> 00:23:11.139
Vikesh K: the idea being. Once you have removed the outlines, this will lead to a better predictions.

273
00:23:11.470 --> 00:23:12.250
Vikesh K: Okay?

274
00:23:14.750 --> 00:23:17.710
Vikesh K: And same thing. You can also do something called

275
00:23:17.740 --> 00:23:19.250
Vikesh K: interquartile method.

276
00:23:19.930 --> 00:23:22.100
Vikesh K: in which, when you have a box plot.

277
00:23:23.750 --> 00:23:28.330
Vikesh K: this distance is called, and basically an Iqr, you calculate the distance.

278
00:23:28.350 --> 00:23:31.339
Vikesh K: Okay, let me put it like this. This is your Iqr.

279
00:23:31.730 --> 00:23:36.859
Vikesh K: so anything which is quarter 3 percentile. Let's say, this is value of 4.

280
00:23:37.030 --> 00:23:41.480
Vikesh K: And then let's say, your intercourtal range is 5. Okay.

281
00:23:41.500 --> 00:23:45.039
Vikesh K: so 4 plus 1.5

282
00:23:45.530 --> 00:23:50.610
Vikesh K: into 5. Whatever that value is, that's your one

283
00:23:51.938 --> 00:23:56.490
Vikesh K: basically extreme limit anything outside that is your

284
00:23:56.540 --> 00:24:01.050
Vikesh K: outlier. So any of these points which is beyond your maximum.

285
00:24:01.160 --> 00:24:04.950
Vikesh K: and and these points on the left hand side, they will be dropped off.

286
00:24:05.770 --> 00:24:10.330
Vikesh K: Okay, that's another way by which you can do the outlier removal.

287
00:24:10.470 --> 00:24:22.649
Vikesh K: So it's up to, you see which one gives the best way. I would say, experiment. That's where you will learn more about the data set and what are the best techniques? Try with both the methods. But these are one of the 2 methods by which you will do the outlier treatment.

288
00:24:23.120 --> 00:24:28.619
Avinash Gangwal: For this also. Is there any inbuilt function just like you calculated z score

289
00:24:29.080 --> 00:24:30.629
Avinash Gangwal: from the stats dot zoom.

290
00:24:30.907 --> 00:24:36.179
Vikesh K: This is more like, you know what what I did here, for example, I've I've written down the code.

291
00:24:36.350 --> 00:24:42.589
Vikesh K: I calculated the 75th percentile point and 25th percentile point

292
00:24:42.770 --> 00:24:45.900
Vikesh K: and calculated the gap between them. Okay, so

293
00:24:45.910 --> 00:24:53.809
Vikesh K: 75th percentile minus 25th percentile will gives you the Iqr that's 21,433.

294
00:24:53.920 --> 00:24:56.760
Vikesh K: Then you calculate the lower bound and upper bound.

295
00:24:57.180 --> 00:24:59.479
Vikesh K: Actually, I have done this. So let me

296
00:25:00.160 --> 00:25:04.910
Vikesh K: okay. So by Iqr method, we lose around 8.5 7% of the data.

297
00:25:05.540 --> 00:25:13.860
Vikesh K: So previously, we we had when we use the other method, that was 1.8%. Here, we lose 10%. Roughly, 9% of the data.

298
00:25:14.340 --> 00:25:21.479
Vikesh K: You also have to be careful if you're losing too much of the data, maybe. Yeah, you should not use it. Okay, so so you, you have to check all these things.

299
00:25:22.253 --> 00:25:25.089
Vikesh K: This is more of an experiment rather than you know.

300
00:25:25.890 --> 00:25:27.680
Vikesh K: Fury says you can use both

301
00:25:28.160 --> 00:25:29.020
Vikesh K: ideally.

302
00:25:29.140 --> 00:25:34.589
Vikesh K: but then you you test and see which one gives you a more reliable estimate and more reliable estimator.

303
00:25:36.040 --> 00:25:41.830
Avinash Gangwal: Based on your experience, how much percentage is more. And we, for example.

304
00:25:42.820 --> 00:25:46.189
Avinash Gangwal: 8.5 7 is too much data to lose.

305
00:25:46.550 --> 00:25:47.990
Avinash Gangwal: Or it's okay.

306
00:25:48.902 --> 00:25:54.639
Vikesh K: See, if you have, maybe lot millions of rows, maybe 9% data is signed.

307
00:25:56.270 --> 00:26:00.210
Vikesh K: But if if your data set already is not a big amount

308
00:26:00.590 --> 00:26:08.600
Vikesh K: maybe 9% is not like, it's quite, quite a lot of data. But the best way would be, you build a model.

309
00:26:08.730 --> 00:26:16.500
Vikesh K: And then, you see which one gives you the best output on your test data set, and we will talk about that later. But that's the best way to check this.

310
00:26:17.740 --> 00:26:25.239
Vikesh K: because it might happen that you have these outliers in your data set, and that's distorting the whole picture. And it's important to remove these

311
00:26:25.790 --> 00:26:27.379
Vikesh K: via this method.

312
00:26:28.720 --> 00:26:29.500
Vikesh K: Okay?

313
00:26:30.300 --> 00:26:34.189
Vikesh K: And then this is how your data set looks like after the outlier removal

314
00:26:34.470 --> 00:26:35.950
Vikesh K: slightly, much better.

315
00:26:37.040 --> 00:26:40.870
Vikesh K: And then again, you can check. You have

316
00:26:42.400 --> 00:26:44.429
Vikesh K: dot describe.

317
00:26:46.200 --> 00:26:54.989
Vikesh K: Now the Max is 75,000. Remember, in the ZZ score method this was 2 25 K. Now, with the maximum which we have is 75,000,

318
00:26:55.080 --> 00:27:02.840
Vikesh K: which maybe it makes sense that you know, if if the car is, if you're still buying a car at 2 25 k, maybe it's too much

319
00:27:03.510 --> 00:27:10.710
Vikesh K: right nobody would buy a second hand car unless until it's really some luxury car and 2 25 k, but yeah, that that

320
00:27:10.910 --> 00:27:27.769
Vikesh K: remember, outlier treatment and missing value. Treatment often requires some domain knowledge. You need to peek into the data and see, hey, what kind of car is being sold at 225 k. Does it even justify? Maybe it's let's say, limbogany or some. It's not very old. Then 225 K. Is fine.

321
00:27:27.910 --> 00:27:34.290
Vikesh K: But maybe if it's a normal sedan and someone is just saying, Oh, it's a luxury, it's a it's a some.

322
00:27:34.300 --> 00:27:43.889
Vikesh K: you know. What does that work? Antique car? And I'm selling it for? 2, 25 K. Maybe it's a wrong price. So you need to have some domain knowledge there ideally for missing value and outlier treatment.

323
00:27:44.000 --> 00:27:47.260
Vikesh K: So always, you know, go deep into that.

324
00:27:48.100 --> 00:27:51.460
Vikesh K: So she says, check quantum outfits and decide, okay, cool.

325
00:27:51.800 --> 00:27:57.230
Vikesh K: So. But but I just want you to be aware of the 2 methods I've listed down here, you know, experiment later on.

326
00:27:57.480 --> 00:28:09.229
Vikesh K: Now, the other things which you might be curious about is, hey? This is what I figured out about the the car price itself. That's how the data set looks like. But what is the relationship with other elements.

327
00:28:09.310 --> 00:28:13.500
Vikesh K: So you have, then you focus on the bivariate analysis and bivariate is.

328
00:28:13.650 --> 00:28:18.780
Vikesh K: first, st is the numerical values. One of the best way is you do the correlation and heat map.

329
00:28:20.510 --> 00:28:25.960
Vikesh K: By the way, here you have both Msrp and Msrp. Log, so ignore that Msrp log for the time being.

330
00:28:26.330 --> 00:28:41.400
Vikesh K: Just focus on Msrp, so you have 0 point 2 1. 1 of the highest is, I believe, engine horsepower. So if your engine horsepower is higher, you have higher chances of an expensive car. Right? They move in the same direction.

331
00:28:41.420 --> 00:28:46.519
Vikesh K: Engine cylinders. Again, 0 point 5 4 number of doors is negative.

332
00:28:46.670 --> 00:28:55.250
Vikesh K: so it could be. You know I've seen those fancy Ferrari cars with only 2 doors maybe those kind of features are there, so the

333
00:28:55.660 --> 00:28:58.490
Vikesh K: usually only the luxury cars might have a

334
00:28:59.771 --> 00:29:03.310
Vikesh K: very high price. Hence maybe it's negative. We need to check

335
00:29:03.410 --> 00:29:06.990
Vikesh K: highway miles per gallon. It's negative. So

336
00:29:07.570 --> 00:29:09.319
Vikesh K: if a car has a

337
00:29:09.440 --> 00:29:10.570
Vikesh K: Hi, I

338
00:29:10.900 --> 00:29:12.190
Vikesh K: mileage.

339
00:29:13.120 --> 00:29:16.410
Vikesh K: It will have a negative impact on its

340
00:29:16.480 --> 00:29:21.529
Vikesh K: like. It moves in the opposite direction to the miles to the minimum selling Price

341
00:29:21.570 --> 00:29:24.779
Vikesh K: city miles again. But maybe this could be because I'm

342
00:29:25.470 --> 00:29:28.039
Vikesh K: luxury. Cars have a very bad

343
00:29:28.390 --> 00:29:32.269
Vikesh K: miles per gallon. Mpg, right? That could be one reason for for.

344
00:29:32.270 --> 00:29:34.190
Avinash Gangwal: But still this is not

345
00:29:34.200 --> 00:29:40.830
Avinash Gangwal: correct. Right doesn't matter what kind of car is. If mileage is more, the Msrp. Should be high.

346
00:29:42.380 --> 00:29:47.249
Vikesh K: If mileage is. Yes, but it could be the fact that you know you have luxury cars

347
00:29:47.280 --> 00:30:00.070
Vikesh K: where mile or maybe let's say, I believe, hummer. I don't know much about us cars, but let's say hummer, which is, which is which. I think it's a decently expensive car, but I don't think it will give you a lot of mileage right? And that distorts the whole picture.

348
00:30:00.760 --> 00:30:02.719
Vikesh K: And then let's say you have rolls, Roy.

349
00:30:02.750 --> 00:30:07.899
Vikesh K: I don't think it's great on mileage. But it's hugely expensive car that will distort the whole picture again.

350
00:30:08.580 --> 00:30:15.459
Vikesh K: So so this is about, yeah. That's why I said, you know, sometimes having some understanding about the domain, and all will give you more insights about it.

351
00:30:16.200 --> 00:30:24.389
Vikesh K: If something looks peculiar and something looks odd, then yes, you start digging deep into it and trying to understand, hey, where? Where do I see these?

352
00:30:24.930 --> 00:30:27.150
Vikesh K: You know. One of the best ways then we can do

353
00:30:27.170 --> 00:30:29.449
Vikesh K: is, let's say you have this. Df.

354
00:30:31.140 --> 00:30:32.330
Vikesh K: you

355
00:30:32.680 --> 00:30:36.550
Vikesh K: basically plot this and then see if we can get some insights.

356
00:30:37.560 --> 00:30:38.610
Vikesh K: you'll have

357
00:30:38.870 --> 00:30:39.990
Vikesh K: Scatter

358
00:30:40.660 --> 00:30:43.549
Vikesh K: X equals to. Let's say we do.

359
00:30:45.820 --> 00:30:47.160
Vikesh K: miles per gallon.

360
00:30:47.630 --> 00:30:48.480
Vikesh K: Oh.

361
00:30:48.770 --> 00:30:49.780
Vikesh K: why.

362
00:30:51.500 --> 00:30:53.080
Vikesh K: Ms. P.

363
00:30:56.200 --> 00:30:56.930
Vikesh K: Okay.

364
00:30:58.240 --> 00:30:59.460
Vikesh K: there is

365
00:30:59.640 --> 00:31:00.820
Vikesh K: one car

366
00:31:02.110 --> 00:31:08.229
Vikesh K: which is very high. But but, for example, let's say, here you see very low mileage.

367
00:31:08.890 --> 00:31:15.360
Vikesh K: and the price is very high. So these would be some luxury cars right? I think they are distorting the whole thing.

368
00:31:15.800 --> 00:31:26.310
Vikesh K: And remember, right now I have. I I think I'm still using the original data set I can remove. I can maybe use the modified one. I haven't touched that, but because that that I'm leaving as an exercise for all of you.

369
00:31:29.740 --> 00:31:40.460
Vikesh K: so that you're curious. You know how the results will look like, but most likely when we remove the outlier. So this will change. These will get dropped, most likely, and then you will have a different picture.

370
00:31:40.590 --> 00:31:43.889
Vikesh K: But these are the these are the cars which are distorting the whole thing.

371
00:31:45.070 --> 00:31:46.020
Vikesh K: make sense.

372
00:31:46.870 --> 00:31:48.440
Vikesh K: others whom I can't see.

373
00:31:48.450 --> 00:31:59.259
Vikesh K: so I have no clue. You don't even give me any visual clue if you're making, if it making sense or not, at least from Shashi and Avina's face. And and you know I can see if I'm making sense or not. Others all good.

374
00:32:00.740 --> 00:32:04.459
Vikesh K: Mike Annu, Preeti, Ambratashika, Vikash, Vijay.

375
00:32:04.910 --> 00:32:09.990
Vijay Chaganti: Yeah, I was following. I can't switch on the video. I was from

376
00:32:10.570 --> 00:32:11.620
Vijay Chaganti: office.

377
00:32:11.970 --> 00:32:16.719
Vikesh K: That's fine. That's fine. If if you're not in the position. That's fine. But yeah, at least, then you tell me.

378
00:32:17.326 --> 00:32:20.099
Vikesh K: in between the things are making sense. Okay.

379
00:32:20.100 --> 00:32:29.069
Ravi: So a question so you only picked up one column right after all the X values to do a scatter plot for making

380
00:32:29.260 --> 00:32:32.569
Ravi: some assessment right? But about other columns

381
00:32:32.670 --> 00:32:37.190
Ravi: do we need to care to go through them them before going further?

382
00:32:37.670 --> 00:32:46.849
Vikesh K: Yeah. So so it's always good, especially if you're killed. For example, Avinash was curious about this one particular aspect. So we delve deep into it to just to see what's happening there.

383
00:32:46.920 --> 00:32:53.179
Vikesh K: But yes, ideally you can. You can have all these charts just to see

384
00:32:53.290 --> 00:32:55.670
Vikesh K: what does the relationship look like.

385
00:32:56.550 --> 00:33:01.679
Vikesh K: always good to have that, at least on your at your own level, to have that investigation being done.

386
00:33:03.050 --> 00:33:12.579
Vikesh K: If you have something interesting, then maybe you put it in your final presentation as well. Right? Remember, this is something, is it? It's it's exactly how you will do a capstone.

387
00:33:12.620 --> 00:33:22.429
Vikesh K: You take a problem statement and you stall solve it step by step. So maybe some of the things are interesting, and then you highlight it there and then you include this in your capstone. Presentation.

388
00:33:23.900 --> 00:33:24.550
Ravi: Okay.

389
00:33:24.850 --> 00:33:31.010
Ravi: So we don't need to worry about doing any Pca or anything we identifying.

390
00:33:31.010 --> 00:33:34.740
Vikesh K: Yeah, yes, ideally. See? That's

391
00:33:34.990 --> 00:33:39.060
Vikesh K: so. The whole machine learning is a very back and forth process.

392
00:33:39.510 --> 00:33:49.480
Vikesh K: maybe Pca will be helpful. But right now, I don't think we have a huge data set. So I'm just 1st model, which I will make with only the numerical columns. And that's like engine

393
00:33:49.490 --> 00:33:58.250
Vikesh K: 1, 2, 3, 4, 5, 6. So, and within that I'm using 5. So 5 columns, I'm using 5 columns to predict, I don't think PC. Is required.

394
00:33:58.960 --> 00:34:00.999
Vikesh K: Pcr might be required when you have

395
00:34:01.310 --> 00:34:10.219
Vikesh K: much more complicated data. But in any case, I I don't want to mix couple couple of things together. So we pick up that maybe complicated data set later on. Then do. Pcr.

396
00:34:10.530 --> 00:34:12.150
Vikesh K: but right now not required.

397
00:34:13.020 --> 00:34:13.960
Vikesh K: That's good.

398
00:34:15.690 --> 00:34:16.600
Vikesh K: All right.

399
00:34:17.336 --> 00:34:30.189
Vikesh K: By the way, another way, which is you can produce the chart, but you know you can just have it in a triangular format, and that for that you need to do some masking, and I also change the color scheme.

400
00:34:30.469 --> 00:34:54.220
Vikesh K: So the same information as you can see. Msrp, what are the values? But some people find it better so so this is another way, how you can produce the heat map. Okay, this is in a triangular format, because some people get confused with this, because numbers essentially get repeated here, 0 point 6 6 here, and you will. The same information is the 6 represented here. So this triangle is actually flipped on the other side.

401
00:34:54.310 --> 00:34:58.560
Vikesh K: So sometimes it's easy, sometimes it's complicated. This is another way. How you can showcase it.

402
00:34:59.050 --> 00:35:04.890
Avinash Gangwal: Once we find the outlier in the mileage, we should remove those right to get.

403
00:35:04.890 --> 00:35:10.159
Vikesh K: Yes, yes, yes, I told you I'm I'm doing this as raw. That's that's left as a homework for all of you.

404
00:35:11.220 --> 00:35:11.960
Vikesh K: Okay.

405
00:35:12.730 --> 00:35:21.179
Vikesh K: I'm doing the easy bits. Tough bits are for you. You're you're doing. You're going to learn this. I'm just telling you the different methods. I want you to experiment it.

406
00:35:21.900 --> 00:35:30.258
Vikesh K: Okay? The other thing. I think Ravi had a question regarding different kind of charts. Pair plot is one strategy by which you can

407
00:35:31.350 --> 00:35:33.889
Vikesh K: have these multiple scatter plots together.

408
00:35:34.010 --> 00:35:51.589
Vikesh K: but be careful about it. Spare plot is computationally very intensive. So when you run it, it will take a lot of time. I just took initial 300 rows. All right. If I take the whole row, every row, it actually becomes very computation intensive, and sometimes

409
00:35:51.610 --> 00:36:03.709
Vikesh K: it may not be very illustratable as well. So it's little hard to figure out some insights from it. Okay, so I want you to be aware about it. But there are times when it's useful. There are times when it's not useful.

410
00:36:03.720 --> 00:36:13.430
Vikesh K: What many students do. They will just produce this copy paste and put it in their slides. Don't do that unless until it's able to convey something interesting

411
00:36:14.507 --> 00:36:21.469
Vikesh K: you know. Don't use pair plot charts like this, or what you, or what you should do is, let's say you find something interesting. Here

412
00:36:21.510 --> 00:36:28.549
Vikesh K: you produce, you reproduce, that's separately, and then specifically put it in the Ppt, and then talk about.

413
00:36:28.560 --> 00:36:31.099
Vikesh K: You know the conclusions you want to draw. All right.

414
00:36:31.370 --> 00:36:35.659
Vikesh K: So, but this is one quick way of producing all the combinations together.

415
00:36:36.990 --> 00:36:38.950
Vikesh K: Okay? So that was on numerical

416
00:36:39.731 --> 00:36:46.559
Vikesh K: and remember, this is still with the outliers. I haven't treated that. I haven't used the non outlier data set.

417
00:36:46.680 --> 00:36:53.970
Vikesh K: Now we will focus on the categorical values. So one easy way is, for example, you have these kind of transmissions.

418
00:36:54.090 --> 00:37:01.950
Vikesh K: Do they have impact on your miles on your price. You can see that you have 5 transmission type.

419
00:37:02.180 --> 00:37:09.199
Vikesh K: One way. One very easy way is when you have the described item, you do a group by the within it.

420
00:37:09.490 --> 00:37:11.119
Vikesh K: Once you do a group buy

421
00:37:11.360 --> 00:37:16.480
Vikesh K: everything you will see is now segmented by the transmission type.

422
00:37:16.710 --> 00:37:28.249
Vikesh K: So automatic, the and I will focus on the person Median prices rather than the main prices right now. So the median prices for automatic is 33,000. Direct drive is 35

423
00:37:28.783 --> 00:37:35.689
Vikesh K: manual is quite cheap, 19,000 unknown. We have to figure out what this is, but that's 2,000

424
00:37:35.900 --> 00:37:39.540
Vikesh K: alright, and there are only 12 values for this not many

425
00:37:40.520 --> 00:37:47.180
Vikesh K: automated manual. I I'm not sure what is automated and manual. That's 1 of the expensive. That's 43,000.

426
00:37:47.660 --> 00:37:54.049
Vikesh K: Okay, so you can get some insight just by combining these values. You can further see this

427
00:37:54.840 --> 00:38:00.159
Vikesh K: by, let's say, a box plot box plot will give you a distribution of prices.

428
00:38:00.300 --> 00:38:06.259
Vikesh K: you know, would allow you to easily see this. So, for example, you can see, automatic has a lot of outliers

429
00:38:06.270 --> 00:38:08.849
Vikesh K: compared to manual or automated manually.

430
00:38:08.950 --> 00:38:12.289
Vikesh K: So it can happen, maybe for this particular subcategory

431
00:38:12.320 --> 00:38:27.519
Vikesh K: your values might be little off, because there are many outliers, and there are too many data points to learn from right. There are outliers on both the ends manual. It fairly follows some decent, and I've used Msrp. Log, and maybe I can also change this.

432
00:38:28.740 --> 00:38:35.340
Vikesh K: And then I see if it's oh, now now you will see a slightly. It's not a very clear picture. Maybe that's why I was using log.

433
00:38:35.480 --> 00:38:36.290
Vikesh K: but

434
00:38:37.010 --> 00:38:45.119
Vikesh K: that that's that's then you can actually see there are also a lot of outliers in the Manual and Automatic. Maybe I should use Msrp. In both of them.

435
00:38:46.160 --> 00:38:48.969
Vikesh K: That will be better. We'll give you a better picture.

436
00:38:49.250 --> 00:38:58.490
Vikesh K: The other chart, which we often use is something called violent plots. Now, the advantage of violent plots is the the one of the disadvantage of box plot is

437
00:38:58.670 --> 00:39:05.779
Vikesh K: in the box. It doesn't tell you the distribution of the data. You know how data values are spread. That's something which

438
00:39:06.433 --> 00:39:15.330
Vikesh K: this. This thing can tell you. So what it tells you is, if there is a peak here, there are more data points at this level compared to this level.

439
00:39:16.020 --> 00:39:20.290
Vikesh K: On the other hand, if this was a box plot, it will show you the whole thing as this.

440
00:39:20.600 --> 00:39:22.160
Vikesh K: So you're clueless.

441
00:39:22.190 --> 00:39:26.059
Vikesh K: it will show you the whole complete box. So you're clueless about the distribution.

442
00:39:26.100 --> 00:39:27.120
Vikesh K: But with

443
00:39:27.633 --> 00:39:34.529
Vikesh K: violent plot it actually gives you a distribution. So that's better. So, for example, if you have a violent plot like this.

444
00:39:34.550 --> 00:39:39.950
Vikesh K: that means your data set has 2 peaks at at this level, one at this level.

445
00:39:40.470 --> 00:39:43.161
Vikesh K: Okay? So so we can be,

446
00:39:45.700 --> 00:39:47.410
Vikesh K: be careful about.

447
00:39:47.750 --> 00:39:52.620
Vikesh K: You know, it depends. If you want to show something interesting, violent plot can be a better one.

448
00:39:53.830 --> 00:39:54.660
Vikesh K: Alright.

449
00:39:57.900 --> 00:39:59.440
Vikesh K: All things good. So far

450
00:39:59.890 --> 00:40:01.420
Vikesh K: you're getting hang of things.

451
00:40:02.080 --> 00:40:12.920
Vikesh K: And then, similarly, you can also run a for loop, and then you can do it for your other categories. All right. I did it only for the transmission, but you can also do it for vehicle size.

452
00:40:13.000 --> 00:40:19.519
Vikesh K: and then you figure it out, how does the relationship look like? Okay? So that's for your practice. I've kept it as a homework.

453
00:40:21.430 --> 00:40:22.810
Vikesh K: Okay, now we.

454
00:40:23.290 --> 00:40:25.690
Vikesh K: So this is the 1st part you

455
00:40:26.460 --> 00:40:37.229
Vikesh K: so far what we have done. Let me sort of revise. We did some cleaning. We looked at the day, you know, understood the univariate level the Msrp.

456
00:40:37.380 --> 00:40:42.200
Vikesh K: Then we did some cleaning, although I'm not used that. That's for you outlier treatment.

457
00:40:42.370 --> 00:40:52.589
Vikesh K: And then we looked at the relationship. So this is the area part. This is more or less. You should spend good amount of time here. Try to understand what your data set is trying to tell you.

458
00:40:53.150 --> 00:40:54.200
Vikesh K: And

459
00:40:54.420 --> 00:41:05.119
Vikesh K: now we will come to the data pre-processing part. Okay? So 1st thing which I'm doing, I will use only selected columns, and I will drop rest of the columns.

460
00:41:05.200 --> 00:41:10.490
Vikesh K: and I will focus only on the numerical columns. I will drop 2 columns, which is

461
00:41:11.100 --> 00:41:15.800
Vikesh K: Msrp. Log. I don't want those columns right now

462
00:41:15.870 --> 00:41:18.500
Vikesh K: these are the columns I'm gonna use. Okay.

463
00:41:19.381 --> 00:41:27.430
Vikesh K: my in engine horsepower engine, cylinder number of doors, highway miles per gallon, city miles per gallon and Msrp is what I'm trying to predict.

464
00:41:33.280 --> 00:41:34.300
Vikesh K: So

465
00:41:34.780 --> 00:41:37.009
Vikesh K: I will show you the numeric column list.

466
00:41:37.020 --> 00:41:38.879
Vikesh K: This is a numeric column list.

467
00:41:39.120 --> 00:41:43.889
Vikesh K: I create a data set, and I will show you how this data set.

468
00:41:44.270 --> 00:41:50.170
Vikesh K: Okay, so this is my data set which I'm going to use on which I'm going to build the model just to keep it simple right now

469
00:41:50.440 --> 00:41:57.850
Vikesh K: and then. You will also see there are some missing values here. Okay, I want you to be just aware about it. But there are some missing values here and there.

470
00:41:58.040 --> 00:42:02.319
Vikesh K: There were many in the categorical, but here there are a couple of missing values.

471
00:42:03.340 --> 00:42:06.560
Vikesh K: Now, the 1st thing which we will do is, do the train test split.

472
00:42:07.360 --> 00:42:13.779
Vikesh K: Okay, the idea of the train press. In practice. You also do 3 things. You make

473
00:42:15.060 --> 00:42:18.720
Vikesh K: you make a trend, you make a validation.

474
00:42:18.830 --> 00:42:21.440
Vikesh K: And then you do a test. Okay.

475
00:42:21.700 --> 00:42:29.330
Vikesh K: train and validation. So TV. And test data, train and validation are used

476
00:42:29.520 --> 00:42:31.160
Vikesh K: for model selection.

477
00:42:31.350 --> 00:42:33.980
Vikesh K: So when you have to basically try different models.

478
00:42:34.150 --> 00:42:37.779
Vikesh K: you will train it on train data validate on the

479
00:42:38.020 --> 00:42:39.469
Vikesh K: a validation set

480
00:42:39.840 --> 00:42:48.659
Vikesh K: only after this process. Once you have finalized something, you will ultimately apply it to the test set. Okay? So that's usually the the proper method.

481
00:42:48.920 --> 00:43:07.579
Vikesh K: I'm trying to keep it simple. Right now. I will just do. Train and test split, I will. And I'm going to use only one method right now, which is linear regression. I'm not checking other methods right now. So I will split the data into train and test. And this is how the original data set looks like this is how, after split, it will look like.

482
00:43:08.740 --> 00:43:09.530
Vikesh K: okay.

483
00:43:10.180 --> 00:43:14.786
Vikesh K: we do it for the simple reason. For example, in in

484
00:43:15.460 --> 00:43:22.629
Vikesh K: college professors used to give you homeworks, and you used to learn you used to practice those homeworks, those examples and learn the pattern.

485
00:43:22.940 --> 00:43:27.959
Vikesh K: Then you used to go to the final exam and give a final exam, which was unseen but similar.

486
00:43:28.050 --> 00:43:32.210
Vikesh K: And we do, we make the algorithms go through the same process.

487
00:43:32.510 --> 00:43:34.460
Vikesh K: The algorithms will learn

488
00:43:34.650 --> 00:43:36.359
Vikesh K: using the train data.

489
00:43:36.440 --> 00:43:43.670
Vikesh K: But when I have to see whether they have really learned or they have just memorized the answers, I will validate on the test data.

490
00:43:44.720 --> 00:43:47.279
Vikesh K: Okay, that's why we do train, template

491
00:43:48.490 --> 00:43:50.480
Vikesh K: any questions or doubts here.

492
00:43:51.310 --> 00:43:55.500
Vikesh K: All of you understand this, the the intuition and the idea behind it.

493
00:43:57.760 --> 00:43:58.480
Vikesh K: Yeah.

494
00:43:58.670 --> 00:43:59.610
Vikesh K: So

495
00:43:59.950 --> 00:44:07.910
Vikesh K: what I will do. So you will see x 1 x 2 x 3 are separately highlighted, y, separately highlighted. And then you break it apart.

496
00:44:09.120 --> 00:44:10.290
Vikesh K: We have

497
00:44:10.340 --> 00:44:11.820
Vikesh K: extreme and widely

498
00:44:12.780 --> 00:44:19.279
Vikesh K: okay. I see a question, Harry, I said, but should have converted here to age with respect to current data.

499
00:44:20.010 --> 00:44:32.499
Vikesh K: Yes, yes, you can do all those feature engineering and convert that to an agent. That's a good point. Yes, right now, I won't do it just to keep it simple. But what Hari has said, is a good point. You can include that later on.

500
00:44:33.330 --> 00:44:34.160
Vikesh K: So

501
00:44:34.420 --> 00:44:36.150
Vikesh K: you have X and Y,

502
00:44:36.250 --> 00:44:47.679
Vikesh K: I separate it out. So if you see your X variable, you have engine, horsepower, engine, cylinder, number of doors, highway miles per gallon and city miles per gallon, right? And then you have y.

503
00:44:47.900 --> 00:44:50.620
Vikesh K: which is your all the prices.

504
00:44:50.970 --> 00:44:55.010
Vikesh K: Alright. So this, these are the 2 things in which you have separated out your data set.

505
00:44:55.510 --> 00:44:56.310
Vikesh K: Then

506
00:44:57.140 --> 00:45:02.039
Vikesh K: you basically use this function from scikit-learn. And maybe I should have

507
00:45:02.050 --> 00:45:05.620
Vikesh K: put it together. But this is the

508
00:45:05.660 --> 00:45:07.580
Vikesh K: this is the thing which I'm using.

509
00:45:07.620 --> 00:45:11.880
Vikesh K: although the best practices put everything on the top. But since we are learning it

510
00:45:12.040 --> 00:45:14.730
Vikesh K: so maybe I will just put it together. Sorry. I'm just

511
00:45:14.960 --> 00:45:17.159
Vikesh K: moving fast. Maybe

512
00:45:19.420 --> 00:45:22.260
Vikesh K: I will put it here. So you do the train test split.

513
00:45:22.560 --> 00:45:27.080
Vikesh K: Can anyone tell me what is meant by test size and random state?

514
00:45:29.440 --> 00:45:32.610
Vikesh K: One by one? Let let me pick up. That would be easy.

515
00:45:33.430 --> 00:45:34.320
Vikesh K: Shikha.

516
00:45:39.740 --> 00:45:40.780
Vikesh K: Number of that.

517
00:45:46.932 --> 00:45:51.500
Namrata: Random state, like true or false, it

518
00:45:52.280 --> 00:45:52.730
Namrata: oh.

519
00:45:53.690 --> 00:45:55.060
Namrata: it's.

520
00:45:57.990 --> 00:45:58.880
Vikesh K: There's

521
00:45:59.660 --> 00:46:01.359
Vikesh K: okay, test size.

522
00:46:04.830 --> 00:46:06.680
Namrata: This size.

523
00:46:09.640 --> 00:46:11.710
Shikha: Maybe the percentage of data.

524
00:46:12.850 --> 00:46:17.330
Vikesh K: Yes. So, Shikhai, you said percentage of data. But percentage of what.

525
00:46:20.710 --> 00:46:23.220
Shikha: The whole data like whatever we are testing on.

526
00:46:23.540 --> 00:46:26.590
Vikesh K: And then what? What it will do to that.

527
00:46:37.550 --> 00:46:39.460
Vikesh K: Mike. You wanted to give it a shot.

528
00:46:46.650 --> 00:46:49.499
Vikesh K: It's fine. If you don't know, I just want you to take a guess

529
00:46:50.050 --> 00:46:52.480
Vikesh K: and be more comfortable in just talking about it.

530
00:46:53.290 --> 00:46:56.420
Harish: Is it more like 20% of the data?

531
00:46:56.570 --> 00:46:59.661
Harish: Is it more like the.

532
00:47:00.420 --> 00:47:02.550
Harish: I'm sorry, is it more like

533
00:47:02.650 --> 00:47:03.720
Harish: you're taking

534
00:47:04.080 --> 00:47:08.480
Harish: like 20% of the data for whatever model testing or you're doing.

535
00:47:08.480 --> 00:47:30.580
Vikesh K: Yes. So I'm assigning 20% of the data to test. That's what I'm specifying here. So the split can be. Usually see, it depends. It can range from 5% idly to 25%, or maybe sometimes even 30. But like, that's stretching it too much. But let's say 5 to 25. So either you have 5, 95, that is 5% to test 95 to train.

536
00:47:30.690 --> 00:47:33.380
Vikesh K: You have 10 or 90.

537
00:47:33.500 --> 00:47:35.040
Vikesh K: You have 20,

538
00:47:35.190 --> 00:47:36.550
Vikesh K: 80,

539
00:47:36.880 --> 00:47:44.259
Vikesh K: you have 70, 25 and 75. Okay, these are the different steps you can do, depending on how much data you have.

540
00:47:44.270 --> 00:47:47.540
Vikesh K: Right now, I've chosen to do 2018.

541
00:47:48.370 --> 00:47:53.271
Vikesh K: So that's 1 you can even maybe, you know, you can cross check with these some of those things

542
00:47:54.560 --> 00:47:55.720
Vikesh K: brand new state.

543
00:47:56.610 --> 00:48:04.079
Namrata: Is it like the false will? Just give one just the 1 1 set kind of the data.

544
00:48:04.150 --> 00:48:10.679
Namrata: But if it is true, maybe we can have some different sets of data to train.

545
00:48:10.930 --> 00:48:15.670
Vikesh K: Okay, so random state won't be true or false. For example, I can use also 23.

546
00:48:16.690 --> 00:48:27.269
Namrata: Okay, yeah, so it is, if it is 0, maybe so, it will like, just give one set of the data in, we can specify how how we want it. More, more sets of data.

547
00:48:27.910 --> 00:48:30.509
Vikesh K: Okay, okay, that's 1 point anyone else.

548
00:48:30.510 --> 00:48:42.659
shashi: 2023, the number 23 gives the same result, irrespective of where I generate the results. I mean, I may take your

549
00:48:42.880 --> 00:48:48.450
shashi: python page and run it here. I will still get the same result, with the same random state.

550
00:48:48.450 --> 00:48:54.090
Vijay Chaganti: When we run multiple iterations it will be the same result if we choose the same number. There.

551
00:48:54.560 --> 00:49:06.229
Vikesh K: Yes. So that's that's good point. So random state is very, very important when you're doing machine learning. So so be remember this, be careful about it. You will also see this in machine learning models. Right now, I'm doing it

552
00:49:06.350 --> 00:49:31.869
Vikesh K: for data split. So what's happening? You know, I'm divided. I'm taking the whole data set. I'm dividing, as you can see in the diagram here, some of it to train some of it to test. Now, the main question is, how do you do it? You do it randomly, so that there's no bias. Right? So you do it randomly. But you also want to control that randomness. So you can control that randomness in in programming languages by setting a random state.

553
00:49:31.900 --> 00:49:34.639
Vikesh K: Usually so R has it. Python has it.

554
00:49:34.740 --> 00:49:41.139
Vikesh K: and even splitting the data has it. So when I so random state the numbers doesn't matter.

555
00:49:41.320 --> 00:49:43.630
Vikesh K: But only thing which is important is that

556
00:49:43.840 --> 00:49:51.270
Vikesh K: you should assign some number to it, and that number now, even if you do the same split, you and me will get the same result.

557
00:49:51.320 --> 00:49:54.120
Vikesh K: So that also ensures a reproducibility.

558
00:49:54.370 --> 00:50:03.039
Vikesh K: Okay, so when you take my code and you try this in your machine like Sashi said, you will get the same split as me, provided you have used the same random state.

559
00:50:03.130 --> 00:50:12.629
Vikesh K: Okay? So there is. Remember, there's a randomness. It's pseudo random in programming language. You can control that randomness and random state allows you to control that.

560
00:50:12.650 --> 00:50:16.740
Vikesh K: Okay, so the number can be 1, 2, 3, 4, 5, 6, anything.

561
00:50:17.100 --> 00:50:21.230
Vikesh K: What matters is your number and my number is same. Then we will get the same split.

562
00:50:21.230 --> 00:50:27.130
Vijay Chaganti: Does does that mean? It is going to choose the same data from the same cells in multiple iteration.

563
00:50:27.130 --> 00:50:33.830
Vikesh K: Yeah, yeah, so it will. Let's say it gives me certain cells. It will choose the same column, same rows for you and same rows for me.

564
00:50:35.510 --> 00:50:38.769
Vikesh K: So you can reproduce my results in essentially

565
00:50:41.220 --> 00:50:42.200
Vikesh K: make sense.

566
00:50:42.480 --> 00:50:51.279
Vikesh K: Yeah, see, it doesn't matter how it randomly devise it. But the what? What is important is that when you re replicate the whole thing.

567
00:50:51.440 --> 00:50:53.210
Vikesh K: you should get the same output.

568
00:50:53.430 --> 00:51:02.990
Vikesh K: Okay, so let's say, now, I will do couple of more pre-processing, like someone said, you should use age from here. I can do that, and then my split should be the same.

569
00:51:03.050 --> 00:51:13.299
Vikesh K: So then, if my model output improves, that's only because of that age variable, not because I, my data was split in a different manner. Okay, so you ensure

570
00:51:13.330 --> 00:51:16.550
Vikesh K: reproducibility and consistency in your data split.

571
00:51:16.590 --> 00:51:19.470
Vikesh K: So random state is a very important concept. Remember that.

572
00:51:19.480 --> 00:51:28.360
Vikesh K: So now, this is how your data set looks like you have around 9,000 rows in train 2,000 2,240 in test.

573
00:51:29.030 --> 00:51:34.920
Vikesh K: and your Y, which is your value, which you're trying to predict, is again 9,000 2,240.

574
00:51:35.070 --> 00:51:35.750
Vikesh K: Okay.

575
00:51:36.490 --> 00:51:37.719
Vikesh K: all good. So far.

576
00:51:39.170 --> 00:51:40.280
Vikesh K: So now.

577
00:51:40.820 --> 00:51:46.599
Vikesh K: now, we focus on the imputation. And now this is a key value, a key thing. You have to remember

578
00:51:46.790 --> 00:51:50.200
Vikesh K: many of the data imputations that you will do.

579
00:51:51.350 --> 00:51:52.360
Vikesh K: Do it

580
00:51:52.370 --> 00:51:55.909
Vikesh K: after you do the train test split? Not before it.

581
00:51:56.580 --> 00:52:09.480
Vikesh K: Okay. So many people do. The imputation of missing values at this stage, when you're doing exploratory data answers, maybe it will. It might be fine. But when you're doing for machine learning, you should always do it after the split.

582
00:52:09.660 --> 00:52:11.760
Vikesh K: Even if you are scaling the data.

583
00:52:12.850 --> 00:52:15.610
Vikesh K: you should do it after the split. Because

584
00:52:16.960 --> 00:52:19.600
Vikesh K: what happens, let's say you're doing

585
00:52:21.400 --> 00:52:23.890
Vikesh K: a mean imputation strategy.

586
00:52:24.250 --> 00:52:25.550
Vikesh K: So column

587
00:52:25.820 --> 00:52:27.060
Vikesh K: has got

588
00:52:27.486 --> 00:52:31.210
Vikesh K: some missing values. I'm missing value here, missing value here, missing value here.

589
00:52:31.260 --> 00:52:33.729
Vikesh K: You calculate the mean of this column.

590
00:52:33.850 --> 00:52:37.720
Vikesh K: and then you say, wherever I have missing values, I will impute

591
00:52:38.060 --> 00:52:39.970
Vikesh K: the mean value there. Okay.

592
00:52:40.060 --> 00:52:42.209
Vikesh K: fair strategy, Mino Media.

593
00:52:42.540 --> 00:52:46.239
Vikesh K: But now the problem is the mean that you calculated

594
00:52:47.110 --> 00:52:51.240
Vikesh K: has the train values and also has the test values.

595
00:52:51.470 --> 00:52:56.649
Vikesh K: So your mean value, the that you calculated has some information from your test.

596
00:52:56.920 --> 00:53:04.899
Vikesh K: So that's a data leakage it's equal into. You're going to give your final exam. And somehow I give you a clue by which you can figure out

597
00:53:05.388 --> 00:53:09.859
Vikesh K: you know what questions are. Gonna come in your final exam. So that's a cheating.

598
00:53:10.120 --> 00:53:13.670
Vikesh K: You don't want that that to happen. So what you want to do

599
00:53:13.720 --> 00:53:15.940
Vikesh K: is, hey? I will

600
00:53:16.060 --> 00:53:20.249
Vikesh K: 1st split the data in my train and then test.

601
00:53:20.400 --> 00:53:21.860
Vikesh K: and then whatever

602
00:53:22.733 --> 00:53:28.229
Vikesh K: values there in train, I will calculate the mean of it, and use that to impute train.

603
00:53:28.310 --> 00:53:30.059
Vikesh K: and as well as test.

604
00:53:32.190 --> 00:53:32.849
Vijay Chaganti: This is quite

605
00:53:33.410 --> 00:53:36.410
Vijay Chaganti: of what we did in data analysis, module.

606
00:53:37.140 --> 00:53:38.620
Vikesh K: Sorry, Vijay, can you please repeat.

607
00:53:38.959 --> 00:53:48.120
Vijay Chaganti: This is quite opposite of what we did in data analysis. Model there. We removed, you know, a missing values before we move to Pca. And

608
00:53:50.020 --> 00:53:50.559
Vijay Chaganti: oh, I mean.

609
00:53:50.560 --> 00:53:57.490
Vikesh K: Yeah, so so yeah, remember this, this machine learning part is actually, even if you're doing. PC, I believe within.

610
00:53:57.700 --> 00:54:00.199
Vikesh K: PC, also, you should follow this practice.

611
00:54:00.810 --> 00:54:21.010
Vikesh K: See that one is little. And also, you know, we can't teach you all the complications in one. Go, we will build step by. So this is, you have understood what's, how do you impute and why it's important. Now, I just want to understand. Now, I just want to add one more sophistication to it. So you do any kind of one more thing which we do is something called standard scalar.

612
00:54:21.120 --> 00:54:24.580
Vikesh K: you know we standardize the value. Have you. Have you all gone through that?

613
00:54:25.950 --> 00:54:27.080
Vikesh K: Yeah. Okay.

614
00:54:27.210 --> 00:54:32.839
Vikesh K: that should also be done after your imputing after your train test split.

615
00:54:33.090 --> 00:54:37.309
Vikesh K: Because again, what will happen if you use the complete data set.

616
00:54:37.400 --> 00:54:39.770
Vikesh K: you're mixing your trade and test together.

617
00:54:39.990 --> 00:54:41.760
Vikesh K: So there is some data leakage.

618
00:54:42.200 --> 00:54:42.960
Vikesh K: Okay, this is.

619
00:54:42.960 --> 00:54:44.400
Vijay Chaganti: They're adding bias to it.

620
00:54:45.680 --> 00:54:46.860
Vikesh K: Vijay. Sorry! Can can you please.

621
00:54:46.860 --> 00:54:50.100
Vijay Chaganti: I mean, I mean to say, when we do

622
00:54:50.420 --> 00:54:55.629
Vijay Chaganti: remove the missing values before before this, that means we are adding bias to the model.

623
00:54:55.980 --> 00:54:59.169
Vikesh K: Yes, yes, yeah. That that's 1 way to put it. Yes.

624
00:55:04.470 --> 00:55:13.560
Vikesh K: Oh, Harry, 42 is just, I think, you know, just people people prefer 42. Yeah, there's no, there's no secret or magic associated with 42.

625
00:55:14.480 --> 00:55:21.213
Vikesh K: I think this has to do with the the hitch. There's a book that hitchhikers galaxy. That guide. I think there's some

626
00:55:21.590 --> 00:55:22.180
Vikesh K: some

627
00:55:24.200 --> 00:55:28.580
Vikesh K: something, some mystery behind it, which even I don't know. But yeah, 42 gets used a lot

628
00:55:29.359 --> 00:55:32.409
Vikesh K: percent of data to be considered for training to.

629
00:55:33.030 --> 00:55:35.310
Vikesh K: Okay. So I rebook 2 points.

630
00:55:35.900 --> 00:55:41.609
Vikesh K: So she gave an answer, nice is, there is a nice process where we can look for all at all. These.

631
00:55:41.890 --> 00:55:51.330
Vikesh K: Matt, you can actually produce, based on what we are designing, you can produce, or towards the end after 2, 3 office hours. Hopefully you will. You will have all the information so you can make these.

632
00:55:51.990 --> 00:56:12.000
Vikesh K: But in in any case, in cyclit learn, we will use something called pipelines later on by design. That will give you a flow diagram. So we'll come to that. That's 1 more level of sophistication. But we will come to that later. But all of you have understood so far why we do the train test split first, st then the imputation.

633
00:56:12.640 --> 00:56:18.270
Vikesh K: The intuition is important. Remember, you can figure out the code later on. But why we do it? That's important.

634
00:56:19.250 --> 00:56:21.080
Vikesh K: Preeti ravi, deep, manish.

635
00:56:21.270 --> 00:56:23.480
Vikesh K: suchita, Matt. All good so far.

636
00:56:24.080 --> 00:56:24.780
Vikesh K: Yep.

637
00:56:27.130 --> 00:56:27.870
Vikesh K: okay.

638
00:56:29.920 --> 00:56:30.910
Vikesh K: So now.

639
00:56:31.640 --> 00:56:32.340
Vikesh K: so

640
00:56:32.720 --> 00:56:34.779
Vikesh K: well, how come? I didn't have that?

641
00:56:36.030 --> 00:56:38.289
Vikesh K: Yes. Oh, this was my.

642
00:56:40.670 --> 00:56:47.929
Vikesh K: okay. So my train data has these many missing values. Test data has these many missing values. Okay, now, one thing which I'm doing. Remember.

643
00:56:48.440 --> 00:56:53.339
Vikesh K: earlier, what used to happen is whenever you used to use a psychic learn

644
00:56:53.470 --> 00:56:57.740
Vikesh K: transformation method. The output used to be a numpy array.

645
00:56:58.490 --> 00:57:14.300
Vikesh K: and the numpy array means all your column. Information gets lost. The data is in a very weird format, and many people complain to cyclone for that. And I think, roughly, a year back they added this one configuration by which the output is in a pandas data frame.

646
00:57:14.490 --> 00:57:24.489
Vikesh K: Okay? So if you don't run this, you will get us. You will get a number as an output. But if you run this you will get the output as a pandas pandas data frame

647
00:57:24.580 --> 00:57:26.599
Vikesh K: which makes your life easy, because

648
00:57:26.650 --> 00:57:36.249
Vikesh K: for for algorithm, it doesn't make a lot of difference, because in any case, pandas is built built on top of numpy. So psychic learn understand that. But for you from a user

649
00:57:36.900 --> 00:57:42.050
Vikesh K: user perspective, from a user's perspective, it just becomes life becomes very easy. Okay.

650
00:57:42.070 --> 00:57:46.370
Vikesh K: I'm using. Let let me use a median rather than median mean.

651
00:57:46.760 --> 00:57:55.120
Vikesh K: So I will use a simple, imputed strategy, which is, first, st I need to, and everything in cyclone, as you would have understood, for now

652
00:57:56.230 --> 00:57:59.209
Vikesh K: runs in 4 steps. First, st you initiate.

653
00:57:59.230 --> 00:58:06.160
Vikesh K: Okay, whatever thing you want to do. You initiate that. And I'm I'm 1st imputing it. Then I'm initiating it.

654
00:58:06.190 --> 00:58:09.670
Vikesh K: Then I fit transform. And then I transform okay.

655
00:58:11.600 --> 00:58:15.339
Vikesh K: anyone can tell me, what's the difference between fit, transform and transform?

656
00:58:18.070 --> 00:58:22.290
Vikesh K: If you remember this, another mystery of cyclone has been solved.

657
00:58:24.070 --> 00:58:28.970
Manish Goenka: Fit is the creation of the model, and transform is transformation of the data based on the model.

658
00:58:29.220 --> 00:58:33.910
Vikesh K: Yes, and then what's the difference? Which is that what you said is fit, transform, or.

659
00:58:33.910 --> 00:58:36.229
Manish Goenka: Fade, transform is the creation of the model.

660
00:58:36.880 --> 00:58:39.531
Manish Goenka: and transform his application of the model.

661
00:58:40.640 --> 00:58:41.260
Vikesh K: Okay?

662
00:58:41.460 --> 00:58:49.120
Vikesh K: So so cycle, learn all the major. Thank you. Manish cycle. Learn all the even the machine learning algorithms that we will try

663
00:58:49.580 --> 00:58:52.590
Vikesh K: by the way, we are towards the end. But I will take

664
00:58:52.800 --> 00:58:56.690
Vikesh K: some more time. 10 more minutes if you can hang on. That would be nice.

665
00:58:59.470 --> 00:59:01.789
Vikesh K: Some people need to drop off. So yeah.

666
00:59:01.830 --> 00:59:10.190
Vikesh K: but what happens in fit transform is it learns the parameters. Okay, that happens in the fit stage. Once you have learned the parameters.

667
00:59:10.220 --> 00:59:18.440
Vikesh K: Then you do the transformation. So remember what I said. When you have train test split. You need to 1st calculate the mean of the train data.

668
00:59:18.490 --> 00:59:22.540
Vikesh K: That is the fit stage. And then you transform your data set

669
00:59:23.360 --> 00:59:31.480
Vikesh K: in the train data. Since you want to learn from train and you want to transform the train, you can actually combine the 2 steps. And that's your fit transform.

670
00:59:31.980 --> 00:59:46.540
Vikesh K: Okay in test. Never, ever use fit transform. In test. It should always be only transform. You don't want to learn from test. You want to just transform the test. Hence it will be only test transform. X test.

671
00:59:46.910 --> 00:59:50.750
Vikesh K: Okay, remember that distinction. You learn the pattern

672
00:59:50.760 --> 00:59:58.179
Vikesh K: of whatever I want to learn the median value only from the train data, never from the test data. Hence it's always transformed.

673
00:59:58.480 --> 01:00:03.659
Vikesh K: I can do this in 2 steps. I can fit first, st and then I can transform. And just

674
01:00:04.239 --> 01:00:08.430
Vikesh K: using a slightly easier method in one go. I will do the fit transformation.

675
01:00:08.550 --> 01:00:10.520
Vikesh K: Okay, but you can even break it apart.

676
01:00:11.010 --> 01:00:11.940
Vikesh K: Sounds good.

677
01:00:15.051 --> 01:00:16.798
Vijay Chaganti: Can you please reiterate on that?

678
01:00:17.180 --> 01:00:22.370
Vijay Chaganti: train data will be used for fit and transform and test data only for transform.

679
01:00:22.370 --> 01:00:38.110
Vikesh K: So fit is basically. And you will see this in your machine learning algorithms as well. Fit is basically to learn from the data. And you are supposed to learn only from the claim data, never from the test data. Because, remember, in real life test data is unknown to you. You can't learn from that.

680
01:00:38.700 --> 01:00:42.069
Vikesh K: So you learn only from the train data. And then you

681
01:00:42.250 --> 01:00:47.929
Vikesh K: do one more thing. You transform the train data, which is wherever I have missing values. I will impute the missing values.

682
01:00:48.400 --> 01:00:49.490
Vikesh K: And then.

683
01:00:49.970 --> 01:00:58.390
Vikesh K: whatever this transformer, whatever this computer has learned, I will use that to transform, to impute in my test data as well.

684
01:01:01.060 --> 01:01:01.850
Vikesh K: Okay?

685
01:01:02.340 --> 01:01:06.929
Vijay Chaganti: That data is used to validate the fit and transform data.

686
01:01:06.930 --> 01:01:21.019
Vikesh K: So here I you here, I learn I use the fit. And then I also transform my data. Here. I transform my test data. Remember, the difference is fit. Transform is only for train transform is for a test. That's the difference.

687
01:01:22.970 --> 01:01:23.620
Vijay Chaganti: Thank you.

688
01:01:24.830 --> 01:01:25.610
Vijay Chaganti: Cool.

689
01:01:25.610 --> 01:01:26.499
Vikesh K: So I do this.

690
01:01:27.150 --> 01:01:27.800
shashi: Here.

691
01:01:28.403 --> 01:01:37.070
shashi: What exactly happens? When we have the impute functions run on it. What exactly, is the mathematical process that happens.

692
01:01:37.470 --> 01:01:43.369
Vikesh K: Okay, so so there, there are 2 I have listed. 2 simple imputer is very simple. That

693
01:01:43.670 --> 01:01:47.310
Vikesh K: you use a median of a column to impute the message

694
01:01:47.330 --> 01:01:48.779
Vikesh K: can also use, you know.

695
01:01:49.290 --> 01:01:51.390
Vikesh K: That's something you can specify.

696
01:01:51.430 --> 01:02:16.429
Vikesh K: Knn. I just have listed here, and I want you to go through the like the documentation. It's good to have. This Knn uses a machine learning method to impute the values it's slightly. But I want. I will cover this once we once you go through the Knn in the course. Okay, but I want you to be aware about it. So either you use a simple method, which is mean? Median. That's why it's called simple imputer.

697
01:02:16.430 --> 01:02:21.630
Vikesh K: The other other method is gain an imputer. And within simple imputer. If you check the theory.

698
01:02:21.910 --> 01:02:22.990
Vikesh K: okay.

699
01:02:23.630 --> 01:02:34.310
Vikesh K: you can actually use a strategy, you can use me, which is you're taking an average or median, or most frequent or constant up to you. So you they give you a couple of options.

700
01:02:35.300 --> 01:02:39.525
shashi: Yeah, but because in our this one we have used

701
01:02:40.287 --> 01:02:53.500
shashi: Knn imputer without knowing we have used the Knn imputer, especially in calculating yield of a crop and things like that. So we have used it in a different programming language kind of calculate average of

702
01:02:53.510 --> 01:02:57.180
shashi: surrounding the plants and then give it the missing value. I think.

703
01:02:57.180 --> 01:03:03.599
Vikesh K: Yeah, that's that's that's a more sophisticated method. But yeah, I just want you to go through that in the theory. And then we will cover that.

704
01:03:04.050 --> 01:03:10.560
Vikesh K: Okay? So now, what we have done? We have gone through all the different steps, at least pre-processing.

705
01:03:10.850 --> 01:03:25.949
Vikesh K: What verifies success after the test data is applied. You can. One of the quick way, Matt. How I checked is I again printed the missing value status. As you can see. There, there are no missing values now. Previously there were some missing values in train and test, and now there are no missing values.

706
01:03:26.100 --> 01:03:28.639
Vikesh K: If I misunderstood your question, let me know, Matt.

707
01:03:29.300 --> 01:03:31.960
Vikesh K: when you talk about success

708
01:03:33.780 --> 01:03:35.160
Vikesh K: tool. So now

709
01:03:35.380 --> 01:03:48.120
Vikesh K: I will build the model. But I will start with the basic model. But before that you have to remember the mean value of Y was 41,000. Okay, just remember that which is like, what is the average price of a car that's around 42,000.

710
01:03:48.610 --> 01:03:51.879
Vikesh K: Now, one of the 1st thing which I will use is something called dummy regression.

711
01:03:51.980 --> 01:03:55.989
Vikesh K: Even when I show you the classification. It's your dummy classification.

712
01:03:56.280 --> 01:03:58.930
Vikesh K: This is useful to set a baseline.

713
01:04:00.210 --> 01:04:04.500
Vikesh K: How it does. If you, if you Google dummy regression.

714
01:04:04.920 --> 01:04:07.109
Vikesh K: it's again a psychic learn method.

715
01:04:07.630 --> 01:04:09.779
Vikesh K: I will do sk learn.

716
01:04:10.750 --> 01:04:13.199
Vikesh K: If you go to dummy regression, it's

717
01:04:13.673 --> 01:04:17.219
Vikesh K: regression that makes prediction using simple rules. Okay.

718
01:04:17.300 --> 01:04:19.570
Vikesh K: this is useful to create a baseline

719
01:04:20.100 --> 01:04:26.870
Vikesh K: and the strategies. Again, you can use is mean median, quantile, constant. Okay. What we will use. I think the default

720
01:04:28.120 --> 01:04:29.999
Vikesh K: default is me.

721
01:04:30.810 --> 01:04:32.260
Vikesh K: So what it says

722
01:04:33.340 --> 01:04:42.700
Vikesh K: it can be a simple idea. So if I ask you to predict the price of a car, you just know the average price of a car. So for every car, you will say 42,000.

723
01:04:43.150 --> 01:04:44.539
Vikesh K: That's the strategy.

724
01:04:45.380 --> 01:04:47.140
Vikesh K: Now the idea is.

725
01:04:47.770 --> 01:04:52.409
Vikesh K: if I use the average as my prediction.

726
01:04:52.470 --> 01:04:59.580
Vikesh K: I will be correct. Sometimes I will be wrong sometimes right, because average is some of all the values divided by the number of values.

727
01:04:59.980 --> 01:05:07.429
Vikesh K: and that will create a baseline. The purpose of doing machine learning is is beating, that is beating your average strategy.

728
01:05:07.790 --> 01:05:09.029
Vikesh K: Because if

729
01:05:09.350 --> 01:05:13.739
Vikesh K: average is good enough, that means the machine learning is not required.

730
01:05:13.780 --> 01:05:21.889
Vikesh K: So you're doing machine learning. You're doing slightly more sophisticated method because you want to break that, you know. Go, do a better job than that, baseline.

731
01:05:21.910 --> 01:05:23.299
Vikesh K: So we will see

732
01:05:23.500 --> 01:05:26.329
Vikesh K: how what is the output of an average. So

733
01:05:26.780 --> 01:05:31.360
Vikesh K: again, the step remains the same. 1st I fit it. I fit always on the train data.

734
01:05:32.000 --> 01:05:39.539
Vikesh K: and then I do. The scoring scoring will tell me the R square value of the dummy regression. I should

735
01:05:40.180 --> 01:05:41.250
Vikesh K: put it

736
01:05:41.940 --> 01:05:44.780
Vikesh K: sorry I have used the wrong

737
01:05:45.330 --> 01:05:48.070
Vikesh K: index here. So I will put here

738
01:05:48.490 --> 01:05:50.160
Vikesh K: like this. Yes.

739
01:05:50.330 --> 01:06:09.549
Vikesh K: the dummy r squared is coming 0 point 0 0. So remember, r squared usually in theory, is from 0 to one. If it's 0, that means your model is not able to explain the reality. If it's 1. Your model is doing a very good job of explaining the reality here, the R square is 0 point 0 0. So that means it's basically a very bad model.

740
01:06:10.540 --> 01:06:18.630
Vikesh K: And the again, the root mean square error, I think. I won't be able to go through the theory part of it. But it's it's basically

741
01:06:18.690 --> 01:06:27.319
Vikesh K: you take all the errors you square it, and then you square root it. Oh, you! You take all the errors, you square it plus it up.

742
01:06:27.340 --> 01:06:34.230
Vikesh K: and then you take a average, and then you do the square root. That's 52,000. So it's pretty bad. So

743
01:06:34.280 --> 01:06:40.389
Vikesh K: your error is way bad than your average price. So you you're off with your prices. Okay?

744
01:06:40.900 --> 01:06:44.880
Vikesh K: And then one of the nice way to see this is, you plot this.

745
01:06:46.630 --> 01:07:01.580
Vikesh K: This is how it looks like. So I have basically all the prices are listed, although it's not the best way to use a plot for this line plot, because it's not some time series kind of chart, but I just wanted to visualize it like this. But remember, this is not the best method.

746
01:07:01.860 --> 01:07:08.789
Vikesh K: and you can see the red line is your prediction. So even the prices are high or low, I'm just predicting one line, which is my red line.

747
01:07:09.500 --> 01:07:10.340
Vikesh K: Alright.

748
01:07:12.340 --> 01:07:24.310
Vikesh K: So cheetah imputation can have some effect. That's true. But if you have done imputation, using the right method ideally, it should be fine, right? You you need. Yes, you need to be careful in imputation.

749
01:07:24.510 --> 01:07:28.940
Vikesh K: but provided you have done it in the, you know careful manner, it should be good.

750
01:07:30.900 --> 01:07:41.940
Vikesh K: Okay, but this is, that's why my model looks very bad. Okay, so now you, a baseline has been set. My root mean, square error was 52,000, which is how wrong I am.

751
01:07:44.430 --> 01:07:46.839
Vikesh K: how wrong I am when I'm doing this. Okay.

752
01:07:46.860 --> 01:07:49.409
Vikesh K: now, I will fit a linear regression model.

753
01:07:49.640 --> 01:07:51.119
Vikesh K: When I run this.

754
01:07:51.430 --> 01:07:53.129
Vikesh K: my R square

755
01:07:53.990 --> 01:08:03.060
Vikesh K: increases marginally. But my at least my root mean square error decreases. It's around 38,000, but still it's bad. It's not a very good model.

756
01:08:03.290 --> 01:08:09.769
Vikesh K: and then, if I plot it again. This is one line plot, at least. You can see some values on top of it. I can maybe do.

757
01:08:10.140 --> 01:08:13.200
Vikesh K: Let's see if this works before 0 point 5.

758
01:08:14.370 --> 01:08:25.599
Vikesh K: Yes, I can actually add Alpha Alpha is basically for transparency levels. If I do change the values of alpha, you can see point on top of each other. So there is. There is some amount of

759
01:08:25.660 --> 01:08:28.840
Vikesh K: overlap. But yeah, some prices I can't predict.

760
01:08:28.920 --> 01:08:33.699
Vikesh K: A better way would be a density plot. Again. You know. You see, the your blue

761
01:08:33.760 --> 01:08:36.130
Vikesh K: is the predicted actual is the red.

762
01:08:36.180 --> 01:08:40.560
Vikesh K: and you can see actual has a very different distribution from your predicted

763
01:08:41.140 --> 01:08:43.659
Vikesh K: again. That's why your R. Squared is very bad.

764
01:08:44.359 --> 01:08:49.900
Vikesh K: and you can also do a histogram of the same thing. This is your actual is, I should add, this

765
01:08:51.790 --> 01:08:54.129
Vikesh K: actual is your red points.

766
01:08:55.810 --> 01:09:01.669
Vikesh K: We put the label later on, and blue is your the predictions. Okay? So there's again a big gap.

767
01:09:02.720 --> 01:09:06.210
Vikesh K: Now, if you are curious. This is how the coefficients look like.

768
01:09:07.399 --> 01:09:13.179
Vikesh K: okay, what is the remember when I said initially, in the linear regression, what you're trying to figure out

769
01:09:13.260 --> 01:09:14.956
Vikesh K: is a is a

770
01:09:18.490 --> 01:09:21.409
Vikesh K: is basically an arithmetic equation.

771
01:09:21.560 --> 01:09:25.229
Vikesh K: So what it says is y equals to price equals to

772
01:09:25.250 --> 01:09:27.239
Vikesh K: your engine horsepower

773
01:09:27.520 --> 01:09:31.389
Vikesh K: so, and your city miles per gallon. So, for example, 4, 31

774
01:09:31.819 --> 01:09:34.629
Vikesh K: into city miles per gallon

775
01:09:34.670 --> 01:09:35.990
Vikesh K: City, Mpg.

776
01:09:36.050 --> 01:09:38.039
Vikesh K: Plus 6 90.

777
01:09:39.000 --> 01:09:40.220
Vikesh K: Sorry I'm using

778
01:09:40.279 --> 01:09:42.309
Vikesh K: this mouse is very horrible.

779
01:09:43.790 --> 01:09:47.350
Vikesh K: I think I should use some other kind of pad for this.

780
01:09:47.520 --> 01:09:50.209
Vikesh K: and this is for highway miles per gallon. Okay.

781
01:09:50.390 --> 01:09:51.569
Vikesh K: but remember.

782
01:09:51.660 --> 01:09:53.600
Vikesh K: the model is not very good.

783
01:09:54.240 --> 01:10:06.289
Vikesh K: And that's also one more. That that's another reason is because we haven't included all the categorical values and that can give you more insights. This is only having made a model using numerical values.

784
01:10:06.720 --> 01:10:12.520
Vikesh K: Then the second thing and that's that's again, I want you to try with the Msrp. Log and see if that improves the results.

785
01:10:12.920 --> 01:10:17.520
Vikesh K: The other thing is categorical values. Now for categorical values.

786
01:10:17.780 --> 01:10:21.350
Vikesh K: What we do is one hot encoding. There are 2 methods to do it.

787
01:10:21.830 --> 01:10:25.110
Vikesh K: One is, you can use scikit-learn, one hot encoder.

788
01:10:25.290 --> 01:10:29.829
Vikesh K: That's 1 method, and I want you to maybe give it a shot. Is that there in the homework

789
01:10:29.910 --> 01:10:32.970
Vikesh K: one hot encoder, has it? Has it been covered right now?

790
01:10:33.150 --> 01:10:34.820
Vikesh K: I don't. I don't remember whether.

791
01:10:34.820 --> 01:10:39.930
Ravi: Yeah, it it covered and both get dummies also got covered in the assignment. So.

792
01:10:39.930 --> 01:10:42.759
Vikesh K: Oh, okay. Oh, that's good. Then. Okay, so then you can do this.

793
01:10:42.920 --> 01:10:44.210
Vikesh K: So you have to

794
01:10:44.842 --> 01:10:49.310
Vikesh K: do this and make. But now be careful here. So, for example.

795
01:10:49.620 --> 01:10:51.368
Vikesh K: I will show you one thing.

796
01:10:55.940 --> 01:10:58.600
Vikesh K: if you just do the columns.

797
01:11:02.330 --> 01:11:06.159
Vikesh K: These are the columns which are categorical columns. Okay, they are not many.

798
01:11:06.470 --> 01:11:11.579
Vikesh K: If if you do, for example, shape of this, these are 8 columns. Okay.

799
01:11:14.090 --> 01:11:15.070
Vikesh K: But

800
01:11:15.510 --> 01:11:21.929
Vikesh K: if I run, if I include each of those columns. And I create a dummies. It will basically create 1,000 columns

801
01:11:22.040 --> 01:11:26.809
Vikesh K: because there are different brand makers. Audi, Bentley, Bugatti. Right?

802
01:11:27.010 --> 01:11:31.850
Vikesh K: So right now, what what I would suggest is, don't include, make

803
01:11:31.880 --> 01:11:33.959
Vikesh K: as one of the categorical values.

804
01:11:34.900 --> 01:11:44.020
Vikesh K: Drop it and then do the dummies. Okay, you 1st use the models. First, st use the categorical values which don't have lot of

805
01:11:44.517 --> 01:11:54.249
Vikesh K: cardinal, which doesn't have a high cardinality. By cardinality, I mean, there are not many different options of each one of them. Okay, so be careful about that.

806
01:11:54.780 --> 01:11:55.520
Vikesh K: And

807
01:11:56.410 --> 01:11:58.180
Vikesh K: I can show it like that.

808
01:12:02.460 --> 01:12:04.070
Vikesh K: Let's see if it works.

809
01:12:13.080 --> 01:12:16.070
Vikesh K: Okay, I will try to get a look, you should. Yeah.

810
01:12:17.090 --> 01:12:21.230
Vikesh K: you can see the unique values of, I should do this

811
01:12:21.870 --> 01:12:25.370
Vikesh K: and unique. Let's see this. Okay. So you can see.

812
01:12:25.430 --> 01:12:30.549
Vikesh K: make has 48 variation model has 915 engine fuel type is again 10

813
01:12:31.067 --> 01:12:37.450
Vikesh K: market category 71 vehicle style is 16, so I would say anything which is more than maybe 6 or 7. Drop it.

814
01:12:37.620 --> 01:12:42.450
Vikesh K: just keep it simple for the time being, at least. Understand how the categorical values are being used.

815
01:12:42.970 --> 01:12:45.479
Vikesh K: So you drop, make model

816
01:12:45.838 --> 01:12:54.159
Vikesh K: you drop vehicle style. You drop market categories and build them on, build a model with the rest of the entries that you have maybe engine fuel type you can use.

817
01:12:54.340 --> 01:12:56.119
Vikesh K: But essentially with this.

818
01:12:56.890 --> 01:12:57.910
Vikesh K: And then

819
01:12:58.388 --> 01:13:03.410
Vikesh K: you see how good your model becomes. What's the improvement? Okay? So that's 1.

820
01:13:03.967 --> 01:13:05.340
Vikesh K: So remember now

821
01:13:05.760 --> 01:13:11.400
Vikesh K: how the improvements come into picture at this stage. Remember, you just have, let's say, linear regression as a method.

822
01:13:11.650 --> 01:13:22.910
Vikesh K: It's mostly by data cleaning and data manipulation. So, for example, there was 1 point made, you can calculate the age column so age could be one. That's feature engineering. You can use log value.

823
01:13:22.950 --> 01:13:29.549
Vikesh K: you can remove the outliers and then test it all right. So these are the methods by which you will improve the output.

824
01:13:29.580 --> 01:13:31.060
Vikesh K: That's 1 step of the thing.

825
01:13:31.560 --> 01:13:34.970
Vikesh K: The other step is, you go for the powerful methods

826
01:13:35.100 --> 01:13:39.090
Vikesh K: which we will talk about in the different, in the different upcoming modules.

827
01:13:39.480 --> 01:13:41.940
Vikesh K: But is the picture clear so far? What we did

828
01:13:44.010 --> 01:13:45.370
Vikesh K: any questions.

829
01:13:45.860 --> 01:13:49.360
Vijay Chaganti: What exactly is happening with dummy regression.

830
01:13:50.500 --> 01:13:53.830
Vikesh K: Okay? So what dummy does? Let's say you have a column?

831
01:13:54.823 --> 01:13:56.009
Vikesh K: Let's say.

832
01:13:56.060 --> 01:13:57.830
Vikesh K: Area.

833
01:13:59.190 --> 01:14:03.090
Vikesh K: okay? And you have. Let's say, New York.

834
01:14:03.610 --> 01:14:05.659
Vikesh K: You have San Francisco

835
01:14:05.930 --> 01:14:09.050
Vikesh K: and you let's say you have Chicago. Okay?

836
01:14:09.360 --> 01:14:16.130
Vikesh K: And this is how your data set is there? But what will happen when dummy? You will create a separate column for New York.

837
01:14:16.500 --> 01:14:19.320
Vikesh K: You will create a separate column for San Francisco.

838
01:14:19.970 --> 01:14:22.440
Vikesh K: You will create a separate column for Chicago.

839
01:14:22.520 --> 01:14:26.330
Vikesh K: So this was New York here. So this will be 1 0 0,

840
01:14:26.660 --> 01:14:28.960
Vikesh K: San Francisco, 0 1 0,

841
01:14:29.010 --> 01:14:33.870
Vikesh K: Chicago, 0 0 1. So your data set will get converted into this format.

842
01:14:34.480 --> 01:14:35.459
Vijay Chaganti: Got it. Got it?

843
01:14:35.830 --> 01:14:36.843
Vijay Chaganti: One shot

844
01:14:38.180 --> 01:14:39.210
Vijay Chaganti: application.

845
01:14:39.760 --> 01:14:40.800
Vijay Chaganti: Yes. So.

846
01:14:41.660 --> 01:14:54.280
Vikesh K: Yes, so this is. This is one hot encoding. So you can see the make column. There is a Alpha Romeo. Then make Aston Martin make audi. So this make column, which has 48, 48 columns will be created only for make.

847
01:14:54.700 --> 01:15:02.179
Vikesh K: Then there would be 10 columns created for engine fuel type, 5 columns created for transmission type driven week.

848
01:15:02.490 --> 01:15:05.320
Vikesh K: Driven wheels will be converted again. 4 columns.

849
01:15:05.350 --> 01:15:09.809
Vikesh K: If you sum it up. It should be a big number, and that's what we get in the end.

850
01:15:12.250 --> 01:15:13.220
Vikesh K: Sounds good.

851
01:15:15.950 --> 01:15:20.359
Vikesh K: Okay. So I left some homework for all of you, because I'm also want you to try it.

852
01:15:20.370 --> 01:15:23.810
Vikesh K: But hopefully, at least, the overall process is clear.

853
01:15:24.090 --> 01:15:26.920
Vikesh K: The main thing which I want you to remember is, first, st

854
01:15:27.580 --> 01:15:35.019
Vikesh K: any kind of pre-processing that you do, which is imputation. Do it after to intersplit. Don't do it before that.

855
01:15:35.800 --> 01:15:36.580
Vikesh K: Okay.

856
01:15:37.930 --> 01:15:46.250
Vikesh K: And what was the main thing. And and then what what is meant by random state and couple of other things. But yeah, the process is more important.

857
01:15:47.750 --> 01:15:49.010
Vikesh K: Any questions?

858
01:15:52.410 --> 01:15:54.130
Vikesh K: Yes, I think there were 2 people.

859
01:15:54.320 --> 01:15:54.910
Vikesh K: Yeah.

860
01:15:54.910 --> 01:16:00.579
Anu.Arun: I quite didn't capture what? Why, we need this simple computer. How is it different from

861
01:16:00.810 --> 01:16:05.710
Anu.Arun: just replacing missing values with whatever the mean or.

862
01:16:07.582 --> 01:16:12.739
Vikesh K: So impute imputation does the same thing. You know, it's it's basically I'm trying to.

863
01:16:12.870 --> 01:16:21.170
Vikesh K: You want to replace a missing value with a mean or median. I did the same thing essentially. I didn't do anything differently. There.

864
01:16:21.850 --> 01:16:24.760
Vikesh K: it's just a scikit-learn method which I'm applying. There.

865
01:16:25.880 --> 01:16:26.530
Anu.Arun: Okay, it.

866
01:16:26.530 --> 01:16:31.537
shashi: I have a real. I have a real life example. What we encountered? When

867
01:16:31.870 --> 01:16:33.630
shashi: we were building system.

868
01:16:33.760 --> 01:16:35.489
shashi: Okay, shall I go ahead?

869
01:16:35.670 --> 01:16:36.780
Vikesh K: Sure. Sure. Yeah.

870
01:16:37.250 --> 01:16:44.950
shashi: Yeah, see, I'm I have in a plot of land I've planted 25 25 plants of tomato.

871
01:16:45.350 --> 01:16:56.060
shashi: and all of them over a period of time. Give me yield, some of them will give 10 pounds of yield, some give 15 pounds of yield, some give 25 pounds of yield, some 12 like that.

872
01:16:56.160 --> 01:16:58.820
shashi: And what happens in one of the area

873
01:16:58.990 --> 01:17:01.320
shashi: cow came and grazed some

874
01:17:01.330 --> 01:17:02.879
shashi: 14 plants.

875
01:17:03.640 --> 01:17:09.419
shashi: Now we have all the traits of all the plants, and we are measuring the quality of the plant

876
01:17:09.770 --> 01:17:12.200
shashi: we can't, we have, we can't ignore the

877
01:17:12.490 --> 01:17:27.700
shashi: till the cow came and ate. We have used the data, but just because cow ate the plant, we can't ignore the rest of the thing. So we to calculate all the values and how good the plant is. We have to put some value to the yield of

878
01:17:27.740 --> 01:17:43.190
shashi: projected yield of a tomato of all those tomato plants. So this is when we use this Knn import what he was mentioning. Those use that kind of function to calculate the predicted yield, and then calculate the statistical analysis for that.

879
01:17:43.720 --> 01:17:58.870
shashi: So you need to use whenever there is missing values, it could be because of error in recording the data, or some natural or any of these kind of things happen and you lose the value. So we have to use certain values to calculate the final result.

880
01:17:59.840 --> 01:18:19.650
Vikesh K: Yes, yes. So so, yeah, so knl. Imputation is slightly more sophisticated form of simple imputation. If you think you require knl imputation again, it becomes very easy that cycle you can actually use knl imputation. I don't think many of you may not have like Shashi. I think you know about Knn. Many other people may not know about Knn, so I didn't show that.

881
01:18:19.710 --> 01:18:23.979
Vikesh K: But I've included that so that you're aware about. You know what's what's happening there.

882
01:18:24.100 --> 01:18:28.480
Vikesh K: But Anu, coming back to your question, does that help? Do you still have a doubt? Here.

883
01:18:29.440 --> 01:18:42.529
Anu.Arun: Yeah, I I guess the question was like, what so it's like a a just assistant level, just in a level of abstraction that we don't some, some that some function is doing it for us, just what we would have done manually

884
01:18:42.570 --> 01:18:47.910
Anu.Arun: calculate the mean or mode. It's just kind of elegantly done for us, kind of a thing.

885
01:18:47.910 --> 01:18:58.130
Vikesh K: Yes, yes, essentially, because either see, when you do the imputation, either one of the very basic simple techniques. Either you will use me or you use medium. I'm doing the same thing here.

886
01:18:58.540 --> 01:19:05.459
Vikesh K: So I'm using this simple imputer. Then I'm fitting it on the train data. I'm saying, Hey, wherever you find a missing value.

887
01:19:06.112 --> 01:19:08.770
Vikesh K: Please fill it up with the median value.

888
01:19:10.140 --> 01:19:12.020
Vikesh K: and I'm doing the same for test.

889
01:19:13.330 --> 01:19:19.350
Vikesh K: But the median value, which is calculated, that's calculated only using train data, not the test data.

890
01:19:20.860 --> 01:19:22.510
Anu.Arun: I understand. Okay, okay.

891
01:19:22.510 --> 01:19:28.820
Vikesh K: Yeah, it just makes it your process easy. And why? By? So you can also use the pandas fill in a

892
01:19:30.570 --> 01:19:33.929
Vikesh K: but you have to do it separately for train and separately for test.

893
01:19:33.990 --> 01:19:38.290
Vikesh K: and that will be little more cumbersome. Cikit-learn makes your job easy.

894
01:19:39.570 --> 01:19:46.630
Anu.Arun: Understood. So if you use 2 different approaches it would be interesting to see what is the missing value, what it, what comes, what it.

895
01:19:46.850 --> 01:19:48.529
Anu.Arun: Each method calculates.

896
01:19:48.530 --> 01:19:58.379
Vikesh K: Yeah, but I see mathematically the each method will give you the same value, because if you calculate Median by hand, or by pandas, or by secular median value, should remain the same.

897
01:19:58.380 --> 01:19:58.970
Anu.Arun: Yeah, yeah.

898
01:19:58.970 --> 01:19:59.910
Vikesh K: That's nuts.

899
01:20:00.040 --> 01:20:22.409
Vikesh K: What is more important in that. And that's 1 of the reasons I do hands on here, because, what is more easy for you when you're building a workflow. Right? You have to build a workflow, you know, step by step. This is how I want to do it. Then cycle, if you use it, will just make your life easier, because the it's it's like, you know what you're doing. It's it's pieces of puzzles you need to put those puzzles pieces of puzzles together.

900
01:20:23.094 --> 01:20:27.839
Vikesh K: If everything is cycle in this part, it just fits together. Very well.

901
01:20:27.930 --> 01:20:29.220
Vikesh K: That's the advantage.

902
01:20:31.570 --> 01:20:33.380
Anu.Arun: Okay, I understand. Thank you.

903
01:20:33.380 --> 01:20:39.730
Vikesh K: I I think we maybe it's not very clear. But as you go through maybe a couple of more modules.

904
01:20:39.740 --> 01:20:47.470
Vikesh K: this will start making sense. This will become more crucial when we reach, when we'll go through something called pipelines, pipelines.

905
01:20:47.550 --> 01:21:00.419
Vikesh K: and column transformers. Then the whole thing will maybe start making more sense. Because, see, right now, I've just worked on my numerical data. But I also have categorical data. So we will slowly build on top of it.

906
01:21:02.250 --> 01:21:05.020
Anu.Arun: Okay, yeah, no, no. Makes sense. Yeah. Got it. Thank you.

907
01:21:05.590 --> 01:21:16.800
Vikesh K: Okay, thank you. Thank you for your question. Okay, just one last thing. And I can still say back if you have more doubts. One thing which I wanted to show you. Why we try multiple methods. Can you? Can you see my slides right now?

908
01:21:18.020 --> 01:21:18.530
Ravi: Yes.

909
01:21:18.530 --> 01:21:19.140
Namrata: Yeah, yeah.

910
01:21:19.140 --> 01:21:21.989
Vikesh K: So, for example, this is one of the things you would like to predict.

911
01:21:22.070 --> 01:21:32.959
Vikesh K: which is miles per gallon and displacement displacement. Think of it as your engine size and power. Right? So you see a negative relationship here, right? It's it's clear to all of you. There's a negative relationship here.

912
01:21:33.100 --> 01:21:52.229
Vikesh K: Now why we use multiple methods. And that's why we that's what we are going to learn in rest of the modules now is because each model will give you a different output. So on the same data set, I fitted a linear regression model which we just studied together. Then we have a decision tree. We have a random forest. We have a Kn model.

913
01:21:52.530 --> 01:21:55.500
Vikesh K: Each one of them will give you a different prediction line.

914
01:21:56.090 --> 01:21:56.900
Vikesh K: Okay.

915
01:21:57.980 --> 01:21:58.990
Vikesh K: so

916
01:21:59.340 --> 01:22:13.729
Vikesh K: each one has its pros and cons, and as you go through different methods you will realize the pros and cons. But the main thing you have to remember the big picture is, each method will try a different way of fitting the data. And then you have to see which method works the best for you.

917
01:22:14.670 --> 01:22:21.749
Vikesh K: Okay, and that's 1 of the reasons mathematicians, statisticians, or machine learning guys had to come up with so many methods

918
01:22:22.210 --> 01:22:28.289
Vikesh K: because they developed one method. Then there, for example, linear model is roughly now, 200 years old, right?

919
01:22:29.011 --> 01:22:34.310
Vikesh K: But then they realize, okay, this is good model. But then, if there are nonlinear patterns.

920
01:22:34.500 --> 01:22:45.020
Vikesh K: it won't do a good job because it just fits a straight line. That's the problem with linear model. It just fits a straight line. Okay? But what if your data set your your pattern is not straight.

921
01:22:45.290 --> 01:22:49.170
Vikesh K: Then they said, Okay, you know, we figured out a method called Decision Tree

922
01:22:49.180 --> 01:22:59.140
Vikesh K: decisionary. Some had some issues. Then they said, Okay, let's do random forest. And then some other. These methods had problem. They said, Okay, let's do knl. Okay.

923
01:22:59.740 --> 01:23:02.940
Vikesh K: So every method has a reason why it exists.

924
01:23:03.020 --> 01:23:12.429
Vikesh K: and the idea being, we will take you through this journey. So that you understand. Okay, these are the things which mathematicians tried, and why? And these are the pros and cons of each method.

925
01:23:12.500 --> 01:23:19.790
Vikesh K: Okay, that's the whole purpose of this rest of the module. Same thing here you. You will see this is a, this is

926
01:23:19.810 --> 01:23:26.080
Vikesh K: a positive relationship. And then you can have multiple lines which line best describes the relationship.

927
01:23:26.630 --> 01:23:28.609
Vikesh K: These are the different methods

928
01:23:29.173 --> 01:23:34.850
Vikesh K: linear method, decision, tree, random forest gain and model. Okay, each will giving you a different picture.

929
01:23:35.870 --> 01:23:40.640
Vikesh K: Classification is about. And I think next week is about classification.

930
01:23:41.780 --> 01:23:44.680
Vikesh K: Classification is splitting the data into areas.

931
01:23:45.260 --> 01:23:49.649
Vikesh K: So these are the your data points, your red and blue. This is what you want to separate out.

932
01:23:49.660 --> 01:23:51.340
Vikesh K: How should you separate out

933
01:23:51.850 --> 01:24:00.169
Vikesh K: nearest neighbors will give you this method decision tree will give you this output. Random Forest will give you this output. Okay, this is like, think about it.

934
01:24:00.654 --> 01:24:09.429
Vikesh K: In your country, let's say there are people, red people, living blue people living okay, or some some animals, red animals or blue animals. How do you divide the area between them?

935
01:24:09.630 --> 01:24:15.719
Vikesh K: Okay, different methods will give you different outputs, and then you have to choose which method gives you the best one.

936
01:24:15.740 --> 01:24:19.960
Vikesh K: And for that, then you choose something called an empire, which is a metric.

937
01:24:20.140 --> 01:24:29.499
Vikesh K: and those are the things we will go through. So cycle. Remember, we, the couple of things. I I just want you to give want to give you this quick, quick overview of cyclone.

938
01:24:29.590 --> 01:24:31.059
Vikesh K: You had transformers

939
01:24:31.110 --> 01:24:33.920
Vikesh K: which helps you to transform the data. We did that today.

940
01:24:33.940 --> 01:24:43.380
Vikesh K: Then you have estimator which allow you to apply the machine learning models. You have matrix some of one you saw today root and square error.

941
01:24:43.410 --> 01:24:49.439
Vikesh K: And then when you have to streamline the whole process, then you have pipelines. And this is how it looks like, essentially.

942
01:24:49.470 --> 01:24:51.050
Vikesh K: you transform the data.

943
01:24:51.080 --> 01:24:57.779
Vikesh K: These are some of the methods you fit models on it. All right. It can be a regression model or classification model.

944
01:24:57.910 --> 01:25:05.829
Vikesh K: Then you check the accuracy of that model by a matrix, or how good the model is, and the whole thing can be streamlined using a pipeline

945
01:25:06.890 --> 01:25:07.670
Vikesh K: all right.

946
01:25:08.070 --> 01:25:19.830
Vikesh K: And this is some sample code for it. Okay? But yeah, this is this is just I want you to be aware of the big picture. So when you do psychic. Learn. These are the different components you will learn of psychic learn.

947
01:25:19.940 --> 01:25:23.889
Vikesh K: Okay, data transformation, fitting the model.

948
01:25:23.990 --> 01:25:28.219
Vikesh K: evaluating the model and making a streamlined process of the whole thing

949
01:25:30.250 --> 01:25:31.120
Vikesh K: cool

950
01:25:32.450 --> 01:25:34.429
Vikesh K: any other doubts or questions.

951
01:25:35.690 --> 01:25:51.989
Vikesh K: By the way, 1 1 request, by the time my information my session comes, there's all of you have filled up the feedback form, so I never get to know whether you like or dislike my sessions, or something which I can improve. So if you can if you can fill in particularly, that would be helpful, or maybe even the past one.

952
01:25:52.090 --> 01:26:01.219
Vikesh K: or or if you can request your teammates also, or like your colleagues in this course. That would be helpful, because I would like to get feedback, even if it's a critical feedback

953
01:26:01.320 --> 01:26:10.860
Vikesh K: or a good feedback to know what's being done correctly, what's not being done correctly. So your feedback is important. Please do that. I know it's it's my session is pretty late.

954
01:26:10.930 --> 01:26:23.819
Vikesh K: but the idea of my session being late is because I tried to go through a case study, and my hope is by this time you would have gone through the material, and we will consolidate all that information together. So that's that's 1 of the reasons why it's on Tuesday.

955
01:26:25.020 --> 01:26:25.860
Vikesh K: Okay.

956
01:26:26.670 --> 01:26:28.650
Vikesh K: yes. Number of that will be endpoints.

957
01:26:29.120 --> 01:26:30.570
Ravi: No, I'm good. Thank you.

958
01:26:31.795 --> 01:26:32.180
Ravi: Yeah.

959
01:26:32.180 --> 01:26:57.051
Namrata: Yeah, because so you showed like the output of the model, right? What we got like 38 k, and 52 k, so which we thought it is not good. Right? So we we can apply again, using different columns. And try this. So what should be the expectation in the end, like the for the results, right like

960
01:26:58.120 --> 01:27:02.389
Vikesh K: Oh, good point! See? A lot of it will depend on what kind of business problem you're solving.

961
01:27:02.680 --> 01:27:03.675
Vikesh K: If

962
01:27:05.140 --> 01:27:16.919
Vikesh K: see in business the best part is if you can predict with 100% accuracy that would be wonderful. But often what it ha! What happens is, maybe you won't have that 100% accuracy. Right? So

963
01:27:17.000 --> 01:27:26.300
Vikesh K: even if you get, let's say around maybe if you're 80% there, 60% there, maybe that's that's good to take a business decision

964
01:27:26.580 --> 01:27:29.305
Vikesh K: because it may happen that

965
01:27:30.980 --> 01:27:38.209
Vikesh K: you may not get your 100 accuracy always, because real life is very complicated. Maybe you're missing an important data set

966
01:27:38.380 --> 01:27:48.820
Vikesh K: or important column, and you don't have that. And your model is not doing a good job. So ultimately it will depend on what kind of decisions you want to take based on it. How crucial those decisions are.

967
01:27:49.120 --> 01:27:54.860
Vikesh K: the more crucial those decisions are, the maybe less assumptions you would like to take.

968
01:27:55.100 --> 01:27:59.759
Vikesh K: and that's that's when you will go, for, you know. So we just tried one simple linear regression

969
01:28:00.380 --> 01:28:09.590
Vikesh K: like I showed you just in this comparison, chart. There are other methods, and more most likely this kind of problem

970
01:28:10.706 --> 01:28:15.830
Vikesh K: would require a, you know, a sophisticated method rather than linear regression.

971
01:28:17.310 --> 01:28:25.340
Namrata: So any of these method we can apply on the same like on the model, and we can see what are the different outputs.

972
01:28:25.340 --> 01:28:28.140
Vikesh K: Yes, the the best part of cyclist learn is.

973
01:28:28.180 --> 01:28:31.439
Vikesh K: once you have figured out the data part, the dating, cleaning part

974
01:28:31.520 --> 01:28:38.190
Vikesh K: applying rest of the models is not very difficult. It's same. You call the model you fit the model, and you predict from the model.

975
01:28:38.300 --> 01:28:44.160
Vikesh K: So that's that's actually quite straightforward. There's something called hyperparameter tuning. We will talk about that later.

976
01:28:44.330 --> 01:28:48.130
Vikesh K: But overall the method will remain the same.

977
01:28:48.770 --> 01:28:49.810
Namrata: And from

978
01:28:49.840 --> 01:28:58.119
Namrata: the from, let's say, all these 4 method, whichever gives us the better percentage, that is our best fitting model.

979
01:28:58.380 --> 01:29:03.759
Vikesh K: Yes. So whatever gives you the best output, you will use it, provided that's what you want. Sometimes.

980
01:29:03.760 --> 01:29:04.360
Namrata: Teams.

981
01:29:04.848 --> 01:29:13.219
Vikesh K: In some industries. Let's say finance. Let's say you're giving out loan, and you're doing a classification who should get a loan and who should not get a loan.

982
01:29:13.320 --> 01:29:21.999
Vikesh K: Let's say you deny a loan to someone, and then, this being us, they will come and sue you right. You should be able to explain your output, your decision to a court.

983
01:29:22.350 --> 01:29:26.999
Vikesh K: Then you don't want to use a sophisticated model which you can't explain to the judge

984
01:29:27.470 --> 01:29:42.369
Vikesh K: right? Then a linear regression or logistic regression would be helpful, and I will talk about those trade-offs. But if your purpose is just for prediction, then you go for as powerful model as possible, and often there is a trade-off. It might be a black box model.

985
01:29:44.080 --> 01:29:46.499
Namrata: Got it? Got it? Yeah, makes sense. Yeah.

986
01:29:46.500 --> 01:29:59.040
Vikesh K: There is also a way around it, and we'll talk about that later. But sharp values and something else. But but right now, what you need to remember is, there often is a trade-off between simple and complex models.

987
01:30:00.050 --> 01:30:00.650
Namrata: Oh.

988
01:30:01.180 --> 01:30:01.880
Namrata: thank you!

989
01:30:01.880 --> 01:30:07.220
shashi: Here. How I my measure of success is since I know the

990
01:30:07.230 --> 01:30:08.769
shashi: output of the

991
01:30:09.524 --> 01:30:19.459
shashi: Test data set. Also, I can compare the predicted and test values, and see how good or how close to accurate, how accurate is my prediction. Correct.

992
01:30:19.800 --> 01:30:24.089
Vikesh K: Yeah, see, test it is, you have to use it at the very end. I didn'.

993
01:30:24.090 --> 01:30:24.760
shashi: Yeah, correct.

994
01:30:25.116 --> 01:30:26.900
Vikesh K: Predict, yeah. All your predictions

995
01:30:27.180 --> 01:30:40.059
Vikesh K: should be based on your train data like, first, st that's the 1st step, correct train data and validation data. We don't have validation data in today's officer. But that's where you do the model selection. And once you have exhausted that.

996
01:30:40.240 --> 01:30:43.110
Vikesh K: and you have chosen your best model. Then you try it on test.

997
01:30:44.050 --> 01:30:47.129
Vikesh K: and then you see how good it does on the test. That's yeah.

998
01:30:47.130 --> 01:30:56.949
shashi: So I, I can compare the out. I mean, from the data, original data, what we have of the test value. What was the actual value for that.

999
01:30:57.220 --> 01:30:58.490
shashi: This. There's a set.

1000
01:30:58.950 --> 01:30:59.580
Vikesh K: Yes.

1001
01:30:59.580 --> 01:31:04.207
shashi: What was the predicted, and see the difference? Variance? What is the variance between my accuracy and

1002
01:31:04.480 --> 01:31:05.380
Vikesh K: Yes, yes.

1003
01:31:05.380 --> 01:31:06.050
shashi: Okay.

1004
01:31:06.500 --> 01:31:07.730
shashi: Thanks. Yeah.

1005
01:31:07.730 --> 01:31:15.599
Vikesh K: This is, this is exactly like, let's say, and then then we will go into more into evaluation. But you know I will keep it. Many people have already dropped off

1006
01:31:16.012 --> 01:31:25.269
Vikesh K: but but I will talk about more in depth, in upcoming officers. So so now the main idea is the more or less the framework which we discussed today. That will remain the same.

1007
01:31:25.670 --> 01:31:28.309
Vikesh K: Only thing which will change is algorithm.

1008
01:31:28.340 --> 01:31:31.080
Vikesh K: But rest of the processes more or less remain the same.

1009
01:31:31.100 --> 01:31:40.210
Vikesh K: So when you do logistic regression, same thing, when you do some other method, same thing, only the algorithm which you will do will change. So so be be.

1010
01:31:40.290 --> 01:31:48.019
Vikesh K: if possible. Again, go through the Jupyter notebook, go a couple of times. I'm pretty sure you may not have understood some 1020, 30% of it.

1011
01:31:48.230 --> 01:31:50.222
Vikesh K: So please go through it.

1012
01:31:51.020 --> 01:31:55.710
Vikash: So we can you save this Jupy Turner to again, because some of the coding which you have done

1013
01:31:55.950 --> 01:31:57.560
Vikash: during explanation.

1014
01:31:57.560 --> 01:32:01.019
Vikesh K: Yeah. In any case, that will be made available to all of you.

1015
01:32:01.060 --> 01:32:04.550
Vikesh K: but I can re upload it and share it right now

1016
01:32:08.140 --> 01:32:09.350
Vikesh K: just give me one second

1017
01:32:11.530 --> 01:32:12.620
Vikesh K: everything I.

1018
01:32:12.830 --> 01:32:21.259
Anu.Arun: Keisha while you're sharing quick so last week there was, they asked us to kind of give a idea for a capstone project.

1019
01:32:21.330 --> 01:32:28.240
Anu.Arun: So the maybe that was a bit too early to ask, because

1020
01:32:28.480 --> 01:32:33.439
Anu.Arun: so I'm kind of still brainstorming what I should really do.

1021
01:32:33.490 --> 01:32:38.200
Anu.Arun: So any advice on like.

1022
01:32:38.960 --> 01:32:41.769
Anu.Arun: where? By? When do we really need a.

1023
01:32:42.240 --> 01:32:51.209
Vikesh K: Yeah, so so so that's a good point anup this is something which we discussed last week. So so what has happened?

1024
01:32:52.239 --> 01:32:56.129
Vikesh K: Berkeley has done a redesign of some of the elements

1025
01:32:56.350 --> 01:33:07.289
Vikesh K: based on the past feedback. They have moved around some certain things, and one of the feedback previously was. Learners wanted to start talking about Capstone as early as possible.

1026
01:33:07.350 --> 01:33:17.529
Vikesh K: So I know this is good for some people who are clear what they want to do, but it can lead to confusion for people who are still figuring out things, and still they haven't gone through the material

1027
01:33:17.938 --> 01:33:25.440
Vikesh K: so what? What? It internally when we were discussing this this was highlighted by Viviana. Because I think she took your office as last week.

1028
01:33:25.490 --> 01:33:31.409
Vikesh K: she said. Maybe it's too early right now. So what we can do you, you can submit it later. You don't have to finalize it.

1029
01:33:31.660 --> 01:33:39.029
Vikesh K: And maybe I will also put together some resources which can help you get some idea on what can be your capstone?

1030
01:33:39.060 --> 01:33:45.789
Vikesh K: See? The best one is, if you can pick up some problem at your company and do that. That is the best way to

1031
01:33:46.340 --> 01:33:48.230
Vikesh K: pick up a problem statement and do it.

1032
01:33:48.390 --> 01:33:51.570
Vikesh K: Because then you solve a problem which is happening at your company

1033
01:33:52.090 --> 01:33:56.800
Vikesh K: for practice. Let me share my, I think all of you can see my screen.

1034
01:33:57.030 --> 01:33:58.597
Vikesh K: This is one.

1035
01:33:59.150 --> 01:34:05.220
Vikesh K: I think I've previously shared this. I'm not sure but this is one place where you can see different problem statements.

1036
01:34:05.360 --> 01:34:09.280
Vikesh K: and maybe that will give you an idea of what kind of capstone problem. You can pick up

1037
01:34:11.050 --> 01:34:17.330
Vikesh K: definitely. If you pick up something from this I will have some guidelines, so don't pick up beginner level, and we will talk about it later.

1038
01:34:17.420 --> 01:34:24.459
Vikesh K: But this can give you some idea on what kind of machine learning problems you can pick up. So let's say, Anu, which industry do you work in? I know.

1039
01:34:25.730 --> 01:34:27.730
Anu.Arun: I'm in silicon photonics

1040
01:34:28.230 --> 01:34:30.079
Vikesh K: That's very specific. I I don't know.

1041
01:34:30.080 --> 01:34:35.560
Anu.Arun: Okay, so semiconductor Ics photonics, semiconductor Ics, so.

1042
01:34:35.770 --> 01:34:38.680
Vikesh K: Yeah, I I doubt that kind of, because it's a very new.

1043
01:34:38.680 --> 01:34:47.535
Anu.Arun: Yeah, actually, we could. My problem is the opposite. Like I, I have many ideas, but I don't know what is feasible, like,

1044
01:34:47.920 --> 01:34:48.890
Vikesh K: So it would be.

1045
01:34:48.890 --> 01:35:08.399
Anu.Arun: Wants to investigate like should I do? In fact, I just submitted my assignment. I wrote 3 things I don't know which one I want to do, and probably so, and when I say I don't know what I want to do, because I don't know the complexity of it, so I don't know if I'll be the end of by the time I do it, whether you know there is enough time to do that, or

1046
01:35:08.490 --> 01:35:11.344
Anu.Arun: it's even feasible, or you know that that kind of

1047
01:35:11.680 --> 01:35:12.950
Anu.Arun: uncertainties.

1048
01:35:12.950 --> 01:35:30.150
Vikesh K: That's a good problem. I understand that that's a that's a fair comment. What you said, and that's 1 of the reasons I try to. Now, I will try to focus on more on these kind of case studies in the office hours, so that you understand, whenever you pick up what kind of problems you can, you will encounter in that. Okay? So today, we picked up this, you, you realize this is

1049
01:35:30.210 --> 01:35:38.150
Vikesh K: this, these are the challenge with numerical columns, categorical columns. The other thing which I would recommend you is to go through these projects.

1050
01:35:39.160 --> 01:35:41.000
Vikesh K: These are mostly questions.

1051
01:35:41.440 --> 01:35:42.060
Anu.Arun: Hmm.

1052
01:35:42.060 --> 01:35:45.360
Vikesh K: But let's say you predict the price of a house. You click on this.

1053
01:35:45.976 --> 01:35:58.810
Vikesh K: They will give you a data set, and they will have some questions and some guidelines on what you can do. So, for example, this is a very simple data set. For example, a data set like this should not be used for capstone. I just want you to be.

1054
01:35:59.170 --> 01:36:02.049
Vikesh K: We'll learn what kind of questions can be answered.

1055
01:36:02.470 --> 01:36:05.120
Vikesh K: So they have given you some certain parameters.

1056
01:36:05.410 --> 01:36:08.430
Vikesh K: And then you have to predict the house price using this

1057
01:36:09.110 --> 01:36:17.940
Vikesh K: alright. So if you go through this, basically, if you go through different kind of problem statements out there. Maybe you will get a hang of things you would like to work on.

1058
01:36:18.790 --> 01:36:19.909
Anu.Arun: Yeah, that makes sense. Yeah, yeah.

1059
01:36:19.910 --> 01:36:20.570
Vikesh K: Thank you.

1060
01:36:20.570 --> 01:36:21.660
Anu.Arun: Helpful. Yeah.

1061
01:36:21.660 --> 01:36:32.850
Vikesh K: You just need to read, maybe things here and there, and that will give you some insight. And and in my next officer I will give you some. You know, all these resources Consolidated. So you can actually go through it. And, you know, pick

1062
01:36:32.890 --> 01:36:34.819
Vikesh K: a problem. Maybe from there.

1063
01:36:35.980 --> 01:36:49.189
Anu.Arun: Yeah, that that would be helpful so 1 1 last thing is like one idea was to do. This is kind of work credited. So we take images of the Ics and kind of use machine learning to say whether we have defects or not.

1064
01:36:49.532 --> 01:36:57.180
Anu.Arun: So it's basically image recognition. What to to see if there is. So is that within the scope of this course.

1065
01:36:58.220 --> 01:37:06.150
Vikesh K: Now. So you can do that. Essentially, it's a machine learning problem. But I if you're new to it, I would say this might become a too sophisticated problem.

1066
01:37:06.670 --> 01:37:07.769
Anu.Arun: I see, I see.

1067
01:37:07.770 --> 01:37:15.859
Vikesh K: Yeah, you can pick. You can pick it up if if you want to do that. I'm fine with it. But I want you to pick up something which you know.

1068
01:37:16.520 --> 01:37:24.539
Vikesh K: See, you're doing this course along with your personal professional life. What if that project is too big? And then, you know you also would have your own work. So

1069
01:37:24.650 --> 01:37:30.170
Vikesh K: so pick up something which is not very easy, not very difficult intermediate level.

1070
01:37:30.780 --> 01:37:36.819
Anu.Arun: Understood. Understood. Yeah, that's kind of what I want that advice on, like, I don't know if that is feasible at all. So that that helps.

1071
01:37:37.030 --> 01:37:39.169
Anu.Arun: Okay, thank you so much.

1072
01:37:40.140 --> 01:37:47.659
Vikesh K: Lovely, happy to help any other questions before we call you today. Sorry I've taken extra time, but I think now my office will be little extra. You have to bear with me, you know.

1073
01:37:47.710 --> 01:37:54.150
Vikesh K: Feel free to drop off at whenever you whenever you can't. You know when it it's over your time.

1074
01:37:54.190 --> 01:37:55.490
Vikesh K: But.

1075
01:37:55.490 --> 01:38:08.419
Namrata: Thanks to you like for giving us this extra time and answering our questions right? Like, Yeah, of course, whoever is busy they will leave. But then they can always refer to the recording and like, get the inputs that will be.

1076
01:38:08.420 --> 01:38:20.689
Vikesh K: Thank you. No, I because I know now this will become tricky now that the course also becomes a little difficult. So I want to solve answers right now as as they come, because I don't want you to have a backlog of answers. So by the time you're

1077
01:38:20.770 --> 01:38:31.159
Vikesh K: in week 9 at least all your questions around till week 8 should be sorted out. Otherwise it will create issues later on. It's like maths. Now, everything builds on top of everything else.

1078
01:38:31.190 --> 01:38:37.479
Vikesh K: Okay, if you don't know your algebra well, tell plus will give you trouble. If you don't know, your tal plus probability will give you trouble.

1079
01:38:37.510 --> 01:38:38.910
Vikesh K: It's the same manager.

1080
01:38:40.730 --> 01:38:42.260
Vikesh K: Alright. So

1081
01:38:42.990 --> 01:38:45.299
Vikesh K: any other questions, if no, we can call it today.

1082
01:38:45.300 --> 01:38:56.489
Shikha: Just one thing, Vikesh, I've submitted my capstone project problem statement. But I'm a little scared because it's too huge, and I have no experience on AI or machine learning.

1083
01:38:56.860 --> 01:38:58.249
Vikesh K: Yeah, I think you can change.

1084
01:38:58.510 --> 01:38:59.110
Vikesh K: We can see.

1085
01:38:59.870 --> 01:39:08.369
Vikesh K: I think, one of the reasons. They put it a little early, because, like, I said. You know learners wanted it to be a bit early, and then at least, you put some thought and think about it.

1086
01:39:09.730 --> 01:39:18.230
Vikesh K: and you know, as you go through the material, you will realize, oh, maybe my problems. It was either too complicated or too simple. So you so you can feel free to.

1087
01:39:18.230 --> 01:39:30.299
Shikha: I think just all the technology, like all the things here in machine learning, are so interesting. So whatever problem statement I was choosing, I was like, Oh, okay, I have 6 problem statements I like. So it was very difficult to finalize one.

1088
01:39:30.840 --> 01:39:32.930
Shikha: But I still have second mind here.

1089
01:39:32.930 --> 01:39:52.419
Vikesh K: So then the best way is, either you pick up something which you are going to solve in your current company, or maybe let's say you want to change jobs. Then what kind of work that company does you pick up something like that? So you make it more practical, so that you have some incentive, so as soon as you finish the project, you can put it in your Cv. And you can show it either to your current company or to a potential company.

1090
01:39:52.470 --> 01:40:01.930
Vikesh K: That's the best way you can, because, see, all of you are doing this for career advancement. I hope right? So make it practical like that. So you'll get get more incentives to do it.

1091
01:40:02.180 --> 01:40:04.610
Shikha: Yeah, sure. Thank you so much. Vikesh, yeah.

1092
01:40:06.800 --> 01:40:07.450
Vikesh K: Cool.

1093
01:40:07.800 --> 01:40:12.370
Vikesh K: Thanks a lot. I I think there are no more questions. If there are.

1094
01:40:12.370 --> 01:40:17.929
Shikha: Sorry. Just one last thing you gave us a pro some homework right in this session.

1095
01:40:17.930 --> 01:40:18.959
Vikesh K: Oh, yeah, that's that's.

1096
01:40:18.960 --> 01:40:24.202
Shikha: Can we go over it? In our next session, just for 1015 min like.

1097
01:40:24.970 --> 01:40:28.120
Shikha: so that we'll know whatever we did is good or not.

1098
01:40:28.120 --> 01:40:32.900
Vikesh K: Sure. So then then, what I want you to do is solve it. And just tell to the whole class, because, yeah.

1099
01:40:32.900 --> 01:40:33.710
Shikha: Everybody.

1100
01:40:33.870 --> 01:40:35.340
Shikha: I don't do it.

1101
01:40:35.340 --> 01:40:40.500
Vikesh K: The problem is next officer, I will focus on the next machine learning algorithm, right? So that's the.

1102
01:40:40.500 --> 01:40:41.480
Shikha: God? Did.

1103
01:40:41.630 --> 01:40:42.980
Vikesh K: Becomes very squeezed.

1104
01:40:43.910 --> 01:40:46.750
Shikha: Sure. Sure. Yeah, I understand. Thank you.

1105
01:40:48.180 --> 01:40:50.190
Anu.Arun: Thank you. Bye-bye. Bye, everyone.

1106
01:40:50.600 --> 01:40:51.370
Vikesh K: Thank you.

1107
01:40:51.980 --> 01:40:54.380
Vikesh K: Cheers bye, bye.
