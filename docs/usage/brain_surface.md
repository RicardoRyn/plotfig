# 脑区图

## 全脑

### 快速出图

脑区图使用了`surfplot`的API，结合图集文件，实现对某块脑区值的绘制。

目前支持图集包括：

1. 人 Glasser图集[^1]
1. 人 BNA图集[^2]
1. 猕猴 CHARM 5-level图集[^3]
1. 猕猴 CHARM 6-level图集[^3]
1. 猕猴 BNA图集[^4]
1. 猕猴 D99图集[^5]
1. 黑猩猩 BNA图集[^6]

例如绘制人类Glasser图集中左脑V1区域值为1，右脑MT区域值为1.5。

[^1]:
    Glasser, M. F., Coalson, T. S., Robinson, E. C., Hacker, C. D., Harwell, J., Yacoub, E., Ugurbil, K., Andersson, J., Beckmann, C. F., Jenkinson, M., Smith, S. M., & Van Essen, D. C. (2016). A multi-modal parcellation of human cerebral cortex. Nature, 536(7615), Article 7615. https://doi.org/10.1038/nature18933
[^2]:
    Fan, L., Li, H., Zhuo, J., Zhang, Y., Wang, J., Chen, L., Yang, Z., Chu, C., Xie, S., Laird, A. R., Fox, P. T., Eickhoff, S. B., Yu, C., & Jiang, T. (2016). The Human Brainnetome Atlas: A New Brain Atlas Based on Connectional Architecture. Cerebral Cortex (New York, N.Y.: 1991), 26(8), 3508–3526. https://doi.org/10.1093/cercor/bhw157
[^3]:
    Jung, B., Taylor, P. A., Seidlitz, J., Sponheim, C., Perkins, P., Ungerleider, L. G., Glen, D., & Messinger, A. (2021). A comprehensive macaque fMRI pipeline and hierarchical atlas. NeuroImage, 235, 117997. https://doi.org/10.1016/j.neuroimage.2021.117997
[^4]:
    Lu, Y., Cui, Y., Cao, L., Dong, Z., Cheng, L., Wu, W., Wang, C., Liu, X., Liu, Y., Zhang, B., Li, D., Zhao, B., Wang, H., Li, K., Ma, L., Shi, W., Li, W., Ma, Y., Du, Z., … Jiang, T. (2024). Macaque Brainnetome Atlas: A multifaceted brain map with parcellation, connection, and histology. Science Bulletin, 69(14), 2241–2259. https://doi.org/10.1016/j.scib.2024.03.031
[^5]:
    Reveley, C., Gruslys, A., Ye, F. Q., Glen, D., Samaha, J., E. Russ, B., Saad, Z., K. Seth, A., Leopold, D. A., & Saleem, K. S. (2017). Three-Dimensional Digital Template Atlas of the Macaque Brain. Cerebral Cortex, 27(9), 4463–4477. https://doi.org/10.1093/cercor/bhw248
[^6]:
    Wang, Y., Cheng, L., Li, D., Lu, Y., Wang, C., Wang, Y., Gao, C., Wang, H., Erichsen, C. T., Vanduffel, W., Hopkins, W. D., Sherwood, C. C., Jiang, T., Chu, C., & Fan, L. (2025). The Chimpanzee Brainnetome Atlas reveals distinct connectivity and gene expression profiles relative to humans. The Innovation, 0(0). https://doi.org/10.1016/j.xinn.2024.100755


??? note "人类Glasser图集所有脑区名字:"
    1. lh_V1
    2. lh_MST
    3. lh_V6
    4. lh_V2
    5. lh_V4
    6. lh_V4
    7. lh_V8
    8. lh_4
    9. lh_3b
    10. lh_FEF
    11. lh_PEF
    12. lh_55b
    13. lh_V4A
    14. lh_RSC
    15. lh_POS2
    16. lh_V7
    17. lh_IPS1
    18. lh_FFC
    19. lh_V3B
    20. lh_LO1
    21. lh_LO2
    22. lh_PIT
    23. lh_MT
    24. lh_A1
    25. lh_PSL
    26. lh_SFL
    27. lh_PCV
    28. lh_STV
    29. lh_7Pm
    30. lh_7m
    31. lh_POS1
    32. lh_23d
    33. lh_v23ab
    34. lh_d23ab
    35. lh_31pv
    36. lh_5m
    37. lh_5mv
    38. lh_23c
    39. lh_5L
    40. lh_24dd
    41. lh_24dv
    42. lh_7AL
    43. lh_SCEF
    44. lh_6ma
    45. lh_7Am
    46. lh_7PL
    47. lh_7PC
    48. lh_LIPv
    49. lh_VIP
    50. lh_MIP
    51. lh_1
    52. lh_2
    53. lh_3a
    54. lh_6d
    55. lh_6mp
    56. lh_6v
    57. lh_p24pr
    58. lh_33pr
    59. lh_a24pr
    60. lh_p32pr
    61. lh_a24
    62. lh_d32
    63. lh_8BM
    64. lh_p32
    65. lh_10r
    66. lh_47m
    67. lh_8Av
    68. lh_8Ad
    69. lh_9m
    70. lh_8BL
    71. lh_9p
    72. lh_10d
    73. lh_8C
    74. lh_44
    75. lh_45
    76. lh_47l
    77. lh_a47r
    78. lh_6r
    79. lh_IFJa
    80. lh_IFJp
    81. lh_IFSp
    82. lh_IFSa
    83. lh_p9-46v
    84. lh_46
    85. lh_a9-46v
    86. lh_9-46d
    87. lh_9a
    88. lh_10v
    89. lh_a10p
    90. lh_10pp
    91. lh_11l
    92. lh_13l
    93. lh_OFC
    94. lh_47s
    95. lh_LIPd
    96. lh_6a
    97. lh_i6-8
    98. lh_s6-8
    99. lh_43
    100. lh_OP4
    101. lh_OP1
    102. lh_OP2-3
    103. lh_52
    104. lh_RI
    105. lh_PFcm
    106. lh_PoI2
    107. lh_TA2
    108. lh_FOP4
    109. lh_MI
    110. lh_Pir
    111. lh_AVI
    112. lh_AAIC
    113. lh_FOP1
    114. lh_FOP3
    115. lh_FOP2
    116. lh_PFt
    117. lh_AIP
    118. lh_EC
    119. lh_PreS
    120. lh_H
    121. lh_ProS
    122. lh_PeEc
    123. lh_STGa
    124. lh_PBelt
    125. lh_A5
    126. lh_PHA1
    127. lh_PHA3
    128. lh_STSda
    129. lh_STSdp
    130. lh_STSvp
    131. lh_TGd
    132. lh_TE1a
    133. lh_TE1p
    134. lh_TE2a
    135. lh_TF
    136. lh_TE2p
    137. lh_PHT
    138. lh_PH
    139. lh_TPOJ1
    140. lh_TPOJ2
    141. lh_TPOJ3
    142. lh_DVT
    143. lh_PGp
    144. lh_IP2
    145. lh_IP1
    146. lh_IP0
    147. lh_PFop
    148. lh_PF
    149. lh_PFm
    150. lh_PGi
    151. lh_PGs
    152. lh_V6A
    153. lh_VMV1
    154. lh_VMV3
    155. lh_PHA2
    156. lh_V4t
    157. lh_FST
    158. lh_V3CD
    159. lh_LO3
    160. lh_VMV2
    161. lh_31pd
    162. lh_31a
    163. lh_VVC
    164. lh_25
    165. lh_s32
    166. lh_pOFC
    167. lh_PoI1
    168. lh_Ig
    169. lh_FOP5
    170. lh_p10p
    171. lh_p47r
    172. lh_TGv
    173. lh_MBelt
    174. lh_LBelt
    175. lh_A4
    176. lh_STSva
    177. lh_TE1m
    178. lh_PI
    179. lh_a32pr
    180. lh_p24
    181. rh_V1
    182. rh_MST
    183. rh_V6
    184. rh_V2
    185. rh_V3
    186. rh_V4
    187. rh_V8
    188. rh_4
    189. rh_3b
    190. rh_FEF
    191. rh_PEF
    192. rh_55b
    193. rh_V3A
    194. rh_RSC
    195. rh_POS2
    196. rh_V7
    197. rh_IPS1
    198. rh_FFC
    199. rh_V3B
    200. rh_LO1
    201. rh_LO2
    202. rh_PIT
    203. rh_MT
    204. rh_A1
    205. rh_PSL
    206. rh_SFL
    207. rh_PCV
    208. rh_STV
    209. rh_7Pm
    210. rh_7m
    211. rh_POS1
    212. rh_23d
    213. rh_v23ab
    214. rh_d23ab
    215. rh_31pv
    216. rh_5m
    217. rh_5mv
    218. rh_23c
    219. rh_5L
    220. rh_24dd
    221. rh_24dv
    222. rh_7AL
    223. rh_SCEF
    224. rh_6ma
    225. rh_7Am
    226. rh_7PL
    227. rh_7PC
    228. rh_LIPv
    229. rh_VIP
    230. rh_MIP
    231. rh_1
    232. rh_2
    233. rh_3a
    234. rh_6d
    235. rh_6mp
    236. rh_6v
    237. rh_p24pr
    238. rh_33pr
    239. rh_a24pr
    240. rh_p32pr
    241. rh_a24
    242. rh_d32
    243. rh_8BM
    244. rh_p32
    245. rh_10r
    246. rh_47m
    247. rh_8Av
    248. rh_8Ad
    249. rh_9m
    250. rh_8BL
    251. rh_9p
    252. rh_10d
    253. rh_8C
    254. rh_44
    255. rh_45
    256. rh_47l
    257. rh_a47r
    258. rh_6r
    259. rh_IFJa
    260. rh_IFJp
    261. rh_IFSp
    262. rh_IFSa
    263. rh_p9-46v
    264. rh_46
    265. rh_a9-46v
    266. rh_9-46d
    267. rh_9a
    268. rh_10v
    269. rh_a10p
    270. rh_10pp
    271. rh_11l
    272. rh_13l
    273. rh_OFC
    274. rh_47s
    275. rh_LIPd
    276. rh_6a
    277. rh_i6-8
    278. rh_s6-8
    279. rh_43
    280. rh_OP4
    281. rh_OP1
    282. rh_OP2-3
    283. rh_52
    284. rh_RI
    285. rh_PFcm
    286. rh_PoI2
    287. rh_TA2
    288. rh_FOP4
    289. rh_MI
    290. rh_Pir
    291. rh_AVI
    292. rh_AAIC
    293. rh_FOP1
    294. rh_FOP3
    295. rh_FOP2
    296. rh_PFt
    297. rh_AIP
    298. rh_EC
    299. rh_PreS
    300. rh_H
    301. rh_ProS
    302. rh_PeEc
    303. rh_STGa
    304. rh_PBelt
    305. rh_A5
    306. rh_PHA1
    307. rh_PHA3
    308. rh_STSda
    309. rh_STSdp
    310. rh_STSvp
    311. rh_TGd
    312. rh_TE1a
    313. rh_TE1p
    314. rh_TE2a
    315. rh_TF
    316. rh_TE2p
    317. rh_PHT
    318. rh_PH
    319. rh_TPOJ1
    320. rh_TPOJ2
    321. rh_TPOJ3
    322. rh_DVT
    323. rh_PGp
    324. rh_IP2
    325. rh_IP1
    326. rh_IP0
    327. rh_PFop
    328. rh_PF
    329. rh_PFm
    330. rh_PGi
    331. rh_PGs
    332. rh_V6A
    333. rh_VMV1
    334. rh_VMV3
    335. rh_PHA2
    336. rh_V4t
    337. rh_FST
    338. rh_V3CD
    339. rh_LO3
    340. rh_VMV2
    341. rh_31pd
    342. rh_31a
    343. rh_VVC
    344. rh_25
    345. rh_s32
    346. rh_pOFC
    347. rh_PoI1
    348. rh_Ig
    349. rh_FOP5
    350. rh_p10p
    351. rh_p47r
    352. rh_TGv
    353. rh_MBelt
    354. rh_LBelt
    355. rh_A4
    356. rh_STSva
    357. rh_TE1m
    358. rh_PI
    359. rh_a32pr
    360. rh_p24

??? note "人类BNA图集所有脑区名字:"
    1. lh_A8m
    2. lh_A8dl
    3. lh_A9l
    4. lh_A6dl
    5. lh_A6m
    6. lh_A9m
    7. lh_A10m
    8. lh_A9/46d
    9. lh_IFJ
    10. lh_A46
    11. lh_A9/46v
    12. lh_A8vl
    13. lh_A6vl
    14. lh_A10l
    15. lh_A44d
    16. lh_IFS
    17. lh_A45c
    18. lh_A45r
    19. lh_A44op
    20. lh_A44v
    21. lh_A14m
    22. lh_A12/47o
    23. lh_A11l
    24. lh_A11m
    25. lh_A13
    26. lh_A12/47l
    27. lh_A4hf
    28. lh_A6cdl
    29. lh_A4ul
    30. lh_A4t
    31. lh_A4tl
    32. lh_A6cvl
    33. lh_A1/2/3ll
    34. lh_A4ll
    35. lh_A38m
    36. lh_A41/42
    37. lh_TE1.0/TE1.2
    38. lh_A22c
    39. lh_A38l
    40. lh_A22r
    41. lh_A21c
    42. lh_A21r
    43. lh_A37dl
    44. lh_aSTS
    45. lh_A20iv
    46. lh_A37elv
    47. lh_A20r
    48. lh_A20il
    49. lh_A37vl
    50. lh_A20cl
    51. lh_A20cv
    52. lh_A20rv
    53. lh_A37mv
    54. lh_A37lv
    55. lh_A35/36r
    56. lh_A35/36c
    57. lh_TL
    58. lh_A28/34
    59. lh_TI
    60. lh_TH
    61. lh_rpSTS
    62. lh_cpSTS
    63. lh_A7r
    64. lh_A7c
    65. lh_A5l
    66. lh_A7pc
    67. lh_A7ip
    68. lh_A39c
    69. lh_A39rd
    70. lh_A40rd
    71. lh_A40c
    72. lh_A39rv
    73. lh_A40rv
    74. lh_A7m
    75. lh_A5m
    76. lh_dmPOS
    77. lh_A31
    78. lh_A1/2/3ulhf
    79. lh_A1/2/3tonIa
    80. lh_A2
    81. lh_A1/2/3tru
    82. lh_G
    83. lh_vIa
    84. lh_dIa
    85. lh_vId/vIg
    86. lh_dIg
    87. lh_dId
    88. lh_A23d
    89. lh_A24rv
    90. lh_A32p
    91. lh_A23v
    92. lh_A24cd
    93. lh_A23c
    94. lh_A32sg
    95. lh_cLinG
    96. lh_rCunG
    97. lh_cCunG
    98. lh_rLinG
    99. lh_vmPOS
    100. lh_mOccG
    101. lh_V5/MT+
    102. lh_OPC
    103. lh_iOccG
    104. lh_msOccG
    105. lh_lsOccG
    106. rh_A8m
    107. rh_A8dl
    108. rh_A9l
    109. rh_A6dl
    110. rh_A6m
    111. rh_A9m
    112. rh_A10m
    113. rh_A9/46d
    114. rh_IFJ
    115. rh_A46
    116. rh_A9/46v
    117. rh_A8vl
    118. rh_A6vl
    119. rh_A10l
    120. rh_A44d
    121. rh_IFS
    122. rh_A45c
    123. rh_A45r
    124. rh_A44op
    125. rh_A44v
    126. rh_A14m
    127. rh_A12/47o
    128. rh_A11l
    129. rh_A11m
    130. rh_A13
    131. rh_A12/47l
    132. rh_A4hf
    133. rh_A6cdl
    134. rh_A4ul
    135. rh_A4t
    136. rh_A4tl
    137. rh_A6cvl
    138. rh_A1/2/3ll
    139. rh_A4ll
    140. rh_A38m
    141. rh_A41/42
    142. rh_TE1.0/TE1.2
    143. rh_A22c
    144. rh_A38l
    145. rh_A22r
    146. rh_A21c
    147. rh_A21r
    148. rh_A37dl
    149. rh_aSTS
    150. rh_A20iv
    151. rh_A37elv
    152. rh_A20r
    153. rh_A20il
    154. rh_A37vl
    155. rh_A20cl
    156. rh_A20cv
    157. rh_A20rv
    158. rh_A37mv
    159. rh_A37lv
    160. rh_A35/36r
    161. rh_A35/36c
    162. rh_TL
    163. rh_A28/34
    164. rh_TI
    165. rh_TH
    166. rh_rpSTS
    167. rh_cpSTS
    168. rh_A7r
    169. rh_A7c
    170. rh_A5l
    171. rh_A7pc
    172. rh_A7ip
    173. rh_A39c
    174. rh_A39rd
    175. rh_A40rd
    176. rh_A40c
    177. rh_A39rv
    178. rh_A40rv
    179. rh_A7m
    180. rh_A5m
    181. rh_dmPOS
    182. rh_A31
    183. rh_A1/2/3ulhf
    184. rh_A1/2/3tonIa
    185. rh_A2
    186. rh_A1/2/3tru
    187. rh_G
    188. rh_vIa
    189. rh_dIa
    190. rh_vId/vIg
    191. rh_dIg
    192. rh_dId
    193. rh_A23d
    194. rh_A24rv
    195. rh_A32p
    196. rh_A23v
    197. rh_A24cd
    198. rh_A23c
    199. rh_A32sg
    200. rh_cLinG
    201. rh_rCunG
    202. rh_cCunG
    203. rh_rLinG
    204. rh_vmPOS
    205. rh_mOccG
    206. rh_V6/MT+
    207. rh_OPC
    208. rh_iOccG
    209. rh_msOccG
    210. rh_lsOccG

??? note "猕猴CHARM 5-level集所有脑区名字:"
    1. lh_area_32
    2. lh_area_25
    3. lh_area_24a_b
    4. lh_area_24c
    5. lh_area_24a_b_prime
    6. lh_area_24c_prime
    7. lh_area_10
    8. lh_area_14
    9. lh_area_11
    10. lh_area_13
    11. lh_area_12m_o
    12. lh_Iam_Iapm
    13. lh_lat_Ia
    14. lh_OLF
    15. lh_G
    16. lh_PrCO
    17. lh_area_8A
    18. lh_area_8B
    19. lh_area_9
    20. lh_area_46d
    21. lh_area_46v_f
    22. lh_area_12r_l
    23. lh_area_45
    24. lh_area_44
    25. lh_M1
    26. lh_PMd
    27. lh_PMv
    28. lh_preSMA
    29. lh_SMA
    30. lh_area_3a_b
    31. lh_areas_1_2
    32. lh_SII
    33. lh_V6
    34. lh_V6A
    35. lh_area_5d
    36. lh_PEa
    37. lh_MIP
    38. lh_fundus_IPS
    39. lh_AIP
    40. lh_LIP
    41. lh_LOP
    42. lh_MST
    43. lh_area_7a_b
    44. lh_area_7op
    45. lh_area_7m
    46. lh_area_31
    47. lh_area_23
    48. lh_area_v23
    49. lh_area_29
    50. lh_area_30
    51. lh_TF_TFO
    52. lh_TH
    53. lh_caudal_ERh
    54. lh_mid_ERh
    55. lh_rostral_ERh
    56. lh_area_35
    57. lh_area_36
    58. lh_TGa
    59. lh_TGd
    60. lh_TGg
    61. lh_TEO
    62. lh_post_TE
    63. lh_ant_TE
    64. lh_TE_in_STSv
    65. lh_ant_STSf
    66. lh_FST
    67. lh_TPO
    68. lh_TAa
    69. lh_STGr
    70. lh_Tpt
    71. lh_parabelt
    72. lh_CL_ML
    73. lh_AL_RTL
    74. lh_CM
    75. lh_RM_RTM
    76. lh_RTp
    77. lh_R_RT
    78. lh_AI
    79. lh_Pi
    80. lh_Ins
    81. lh_Ri
    82. lh_MT
    83. lh_V4d
    84. lh_V4v
    85. lh_V3d_V3A
    86. lh_V3v
    87. lh_V2
    88. lh_V1
    89. rh_area_32
    90. rh_area_25
    91. rh_area_24a_b
    92. rh_area_24c
    93. rh_area_24a_b_prime
    94. rh_area_24c_prime
    95. rh_area_10
    96. rh_area_14
    97. rh_area_11
    98. rh_area_13
    99. rh_area_12m_o
    100. rh_Iam_Iapm
    101. rh_lat_Ia
    102. rh_OLF
    103. rh_G
    104. rh_PrCO
    105. rh_area_8A
    106. rh_area_8B
    107. rh_area_9
    108. rh_area_46d
    109. rh_area_46v_f
    110. rh_area_12r_l
    111. rh_area_45
    112. rh_area_44
    113. rh_M1
    114. rh_PMd
    115. rh_PMv
    116. rh_preSMA
    117. rh_SMA
    118. rh_area_3a_b
    119. rh_areas_1_2
    120. rh_SII
    121. rh_V6
    122. rh_V6A
    123. rh_area_5d
    124. rh_PEa
    125. rh_MIP
    126. rh_fundus_IPS
    127. rh_AIP
    128. rh_LIP
    129. rh_LOP
    130. rh_MST
    131. rh_area_7a_b
    132. rh_area_7op
    133. rh_area_7m
    134. rh_area_31
    135. rh_area_23
    136. rh_area_v23
    137. rh_area_29
    138. rh_area_30
    139. rh_TF_TFO
    140. rh_TH
    141. rh_caudal_ERh
    142. rh_mid_ERh
    143. rh_rostral_ERh
    144. rh_area_35
    145. rh_area_36
    146. rh_TGa
    147. rh_TGd
    148. rh_TGg
    149. rh_TEO
    150. rh_post_TE
    151. rh_ant_TE
    152. rh_TE_in_STSv
    153. rh_ant_STSf
    154. rh_FST
    155. rh_TPO
    156. rh_TAa
    157. rh_STGr
    158. rh_Tpt
    159. rh_parabelt
    160. rh_CL_ML
    161. rh_AL_RTL
    162. rh_CM
    163. rh_RM_RTM
    164. rh_RTp
    165. rh_R_RT
    166. rh_AI
    167. rh_Pi
    168. rh_Ins
    169. rh_Ri
    170. rh_MT
    171. rh_V4d
    172. rh_V4v
    173. rh_V3d_V3A
    174. rh_V3v
    175. rh_V2
    176. rh_V1

??? note "猕猴CHARM 6-level集所有脑区名字:"
    1. lh_area_32
    2. lh_area_25
    3. lh_area_24a
    4. lh_area_24b
    5. lh_area_24c
    6. lh_area_24a_prime
    7. lh_area_24b_prime
    8. lh_area_24c_prime
    9. lh_area_10mr
    10. lh_area_10mc
    11. lh_area_10o
    12. lh_area_14r
    13. lh_area_14c
    14. lh_area_11m
    15. lh_area_11l
    16. lh_area_13a_b
    17. lh_area_13m
    18. lh_area_13l
    19. lh_area_12m
    20. lh_area_12o
    21. lh_Iam_Iapm
    22. lh_Iai
    23. lh_Ial
    24. lh_Iapl
    25. lh_AON_TTv
    26. lh_OT_Pir
    27. lh_G
    28. lh_PrCO
    29. lh_area_8Ad
    30. lh_area_8Av
    31. lh_area_8Bd
    32. lh_area_8Bm
    33. lh_area_8Bs
    34. lh_area_9d
    35. lh_area_9m
    36. lh_area_46d
    37. lh_area_46f
    38. lh_area_46v
    39. lh_area_12l
    40. lh_area_12r
    41. lh_area_45a
    42. lh_area_45b
    43. lh_area_44
    44. lh_M1
    45. lh_PMdc
    46. lh_PMdr
    47. lh_F4
    48. lh_F5
    49. lh_preSMA
    50. lh_SMA
    51. lh_area_3a_b
    52. lh_areas_1_2
    53. lh_SII
    54. lh_V6
    55. lh_V6Av
    56. lh_V6Ad
    57. lh_PEc_PEci
    58. lh_PE
    59. lh_PEa
    60. lh_MIP
    61. lh_VIP
    62. lh_PIP
    63. lh_AIP
    64. lh_LIPd
    65. lh_LIPv
    66. lh_LOP
    67. lh_MST
    68. lh_area_7a
    69. lh_area_7b
    70. lh_area_7op
    71. lh_area_7m
    72. lh_area_31
    73. lh_area_23a
    74. lh_area_23b
    75. lh_area_23c
    76. lh_area_v23
    77. lh_area_29
    78. lh_area_30
    79. lh_TFO
    80. lh_TF
    81. lh_TH
    82. lh_EC
    83. lh_ECL
    84. lh_mid_ERh
    85. lh_rostral_ERh
    86. lh_area_35
    87. lh_area_36c
    88. lh_area_36r_p
    89. lh_TGa
    90. lh_TGdd
    91. lh_TGvd
    92. lh_TGdg
    93. lh_TGvg
    94. lh_TGsts
    95. lh_TEO
    96. lh_TEpv
    97. lh_TEpd
    98. lh_TEav
    99. lh_TEad
    100. lh_TEm
    101. lh_TEa
    102. lh_IPa
    103. lh_PGa
    104. lh_FST
    105. lh_TPO
    106. lh_TAa
    107. lh_STGr
    108. lh_Tpt
    109. lh_CPB
    110. lh_RPB
    111. lh_CL
    112. lh_ML
    113. lh_AL
    114. lh_RTL
    115. lh_CM
    116. lh_RM
    117. lh_RTM
    118. lh_RTp
    119. lh_R
    120. lh_RT
    121. lh_AI
    122. lh_Pi
    123. lh_Ia_Id
    124. lh_Ig
    125. lh_Ri
    126. lh_MT
    127. lh_V4d
    128. lh_V4v
    129. lh_V3A
    130. lh_V3d
    131. lh_V3v
    132. lh_possibly_V2
    133. lh_clearly_V2
    134. lh_V1
    135. rh_area_32
    136. rh_area_25
    137. rh_area_24a
    138. rh_area_24b
    139. rh_area_24c
    140. rh_area_24a_prime
    141. rh_area_24b_prime
    142. rh_area_24c_prime
    143. rh_area_10mr
    144. rh_area_10mc
    145. rh_area_10o
    146. rh_area_14r
    147. rh_area_14c
    148. rh_area_11m
    149. rh_area_11l
    150. rh_area_13a_b
    151. rh_area_13m
    152. rh_area_13l
    153. rh_area_12m
    154. rh_area_12o
    155. rh_Iam_Iapm
    156. rh_Iai
    157. rh_Ial
    158. rh_Iapl
    159. rh_AON_TTv
    160. rh_OT_Pir
    161. rh_G
    162. rh_PrCO
    163. rh_area_8Ad
    164. rh_area_8Av
    165. rh_area_8Bd
    166. rh_area_8Bm
    167. rh_area_8Bs
    168. rh_area_9d
    169. rh_area_9m
    170. rh_area_46d
    171. rh_area_46f
    172. rh_area_46v
    173. rh_area_12l
    174. rh_area_12r
    175. rh_area_45a
    176. rh_area_45b
    177. rh_area_44
    178. rh_M1
    179. rh_PMdc
    180. rh_PMdr
    181. rh_F4
    182. rh_F5
    183. rh_preSMA
    184. rh_SMA
    185. rh_area_3a_b
    186. rh_areas_1_2
    187. rh_SII
    188. rh_V6
    189. rh_V6Av
    190. rh_V6Ad
    191. rh_PEc_PEci
    192. rh_PE
    193. rh_PEa
    194. rh_MIP
    195. rh_VIP
    196. rh_PIP
    197. rh_AIP
    198. rh_LIPd
    199. rh_LIPv
    200. rh_LOP
    201. rh_MST
    202. rh_area_7a
    203. rh_area_7b
    204. rh_area_7op
    205. rh_area_7m
    206. rh_area_31
    207. rh_area_23a
    208. rh_area_23b
    209. rh_area_23c
    210. rh_area_v23
    211. rh_area_29
    212. rh_area_30
    213. rh_TFO
    214. rh_TF
    215. rh_TH
    216. rh_EC
    217. rh_ECL
    218. rh_mid_ERh
    219. rh_rostral_ERh
    220. rh_area_35
    221. rh_area_36c
    222. rh_area_36r_p
    223. rh_TGa
    224. rh_TGdd
    225. rh_TGvd
    226. rh_TGdg
    227. rh_TGvg
    228. rh_TGsts
    229. rh_TEO
    230. rh_TEpv
    231. rh_TEpd
    232. rh_TEav
    233. rh_TEad
    234. rh_TEm
    235. rh_TEa
    236. rh_IPa
    237. rh_PGa
    238. rh_FST
    239. rh_TPO
    240. rh_TAa
    241. rh_STGr
    242. rh_Tpt
    243. rh_CPB
    244. rh_RPB
    245. rh_CL
    246. rh_ML
    247. rh_AL
    248. rh_RTL
    249. rh_CM
    250. rh_RM
    251. rh_RTM
    252. rh_RTp
    253. rh_R
    254. rh_RT
    255. rh_AI
    256. rh_Pi
    257. rh_Ia_Id
    258. rh_Ig
    259. rh_Ri
    260. rh_MT
    261. rh_V4d
    262. rh_V4v
    263. rh_V3A
    264. rh_V3d
    265. rh_V3v
    266. rh_possibly_V2
    267. rh_clearly_V2
    268. rh_V1

??? note "猕猴BNA集所有脑区名字:"
    1. lh_FP_d
    2. lh_FP_m
    3. lh_FP_v
    4. lh_SFG_rm
    5. lh_SFG_cm
    6. lh_SFG_r
    7. lh_SFG_ri
    8. lh_SFG_ci
    9. lh_SFG_c
    10. lh_IFG_rd
    11. lh_IFG_cd
    12. lh_IFG_cv
    13. lh_IFG_iv
    14. lh_IFG_rv
    15. lh_OrG_rm
    16. lh_OrG_cm
    17. lh_OrG_ri
    18. lh_OrG_ci
    19. lh_OrG_rl
    20. lh_OrG_cl
    21. lh_M1_v
    22. lh_M1_i
    23. lh_M1_d
    24. lh_M1_m
    25. lh_PM_rd
    26. lh_PM_cd
    27. lh_PM_i
    28. lh_PM_cv
    29. lh_PM_rv
    30. lh_PM_rm
    31. lh_PM_cm
    32. lh_PoCG_dm
    33. lh_PoCG_d
    34. lh_PoCG_i
    35. lh_PoCG_v
    36. lh_FPO_r
    37. lh_FPO_ri
    38. lh_FPO_ci
    39. lh_FPO_c
    40. lh_SPL_rv
    41. lh_SPL_iv
    42. lh_SPL_cv
    43. lh_SPL_rd
    44. lh_SPL_cd
    45. lh_SPL_m
    46. lh_IPL_sr
    47. lh_IPL_sri
    48. lh_IPL_sci
    49. lh_IPL_sc
    50. lh_IPL_gr
    51. lh_IPL_gri
    52. lh_IPL_gci
    53. lh_IPL_gc
    54. lh_PrCu_vr
    55. lh_PrCu_dr
    56. lh_PrCu_dc
    57. lh_PrCu_di
    58. lh_PrCu_vi
    59. lh_PrCu_vc
    60. lh_PrL_d
    61. lh_PrL_i
    62. lh_PrL_STS
    63. lh_PrL_v
    64. lh_SFL_r
    65. lh_SFL_i
    66. lh_STG_gc
    67. lh_STG_gr
    68. lh_STG_gri
    69. lh_STG_gci
    70. lh_STSU_rEx
    71. lh_STSU_cEx
    72. lh_STSU_r
    73. lh_STSU_ri
    74. lh_STSU_ci
    75. lh_STSU_c
    76. lh_STSL_r
    77. lh_STSL_cIn
    78. lh_STSL_cEx
    79. lh_ITG_gr
    80. lh_ITG_gdc
    81. lh_ITG_gvc
    82. lh_PHG_r
    83. lh_PHG_mi
    84. lh_PHG_li
    85. lh_PHG_cm
    86. lh_PHG_cl
    87. lh_TP_vr
    88. lh_TP_mr
    89. lh_TP_lr
    90. lh_TP_dr
    91. lh_TP_cEx
    92. lh_TP_cIn
    93. lh_V1_cm
    94. lh_V1_dl
    95. lh_V1_vl
    96. lh_V1_mvi
    97. lh_V1_mdi
    98. lh_V1_rm
    99. lh_V2_l
    100. lh_V2_d
    101. lh_V2_v
    102. lh_V2_dm
    103. lh_V2_vm
    104. lh_VMO_l
    105. lh_VMO_i
    106. lh_VMO_m
    107. lh_INS_vr
    108. lh_INS_dr
    109. lh_INS_ri
    110. lh_INS_v
    111. lh_INS_ci
    112. lh_INS_c
    113. lh_CG_vr
    114. lh_CG_ir
    115. lh_CG_dr
    116. lh_CG_idr
    117. lh_CG_idc
    118. lh_CG_ivr
    119. lh_CG_ivc
    120. lh_CG_dc
    121. lh_CG_vc
    122. lh_CG_RSr
    123. lh_CG_RSi
    124. lh_CG_RSc
    125. rh_FP_d
    126. rh_FP_m
    127. rh_FP_v
    128. rh_SFG_rm
    129. rh_SFG_cm
    130. rh_SFG_r
    131. rh_SFG_ri
    132. rh_SFG_ci
    133. rh_SFG_c
    134. rh_IFG_rd
    135. rh_IFG_cd
    136. rh_IFG_cv
    137. rh_IFG_iv
    138. rh_IFG_rv
    139. rh_OrG_rm
    140. rh_OrG_cm
    141. rh_OrG_ri
    142. rh_OrG_ci
    143. rh_OrG_rl
    144. rh_OrG_cl
    145. rh_M1_v
    146. rh_M1_i
    147. rh_M1_d
    148. rh_M1_m
    149. rh_PM_rd
    150. rh_PM_cd
    151. rh_PM_i
    152. rh_PM_cv
    153. rh_PM_rv
    154. rh_PM_rm
    155. rh_PM_cm
    156. rh_PoCG_dm
    157. rh_PoCG_d
    158. rh_PoCG_i
    159. rh_PoCG_v
    160. rh_FPO_r
    161. rh_FPO_ri
    162. rh_FPO_ci
    163. rh_FPO_c
    164. rh_SPL_rv
    165. rh_SPL_iv
    166. rh_SPL_cv
    167. rh_SPL_rd
    168. rh_SPL_cd
    169. rh_SPL_m
    170. rh_IPL_sr
    171. rh_IPL_sri
    172. rh_IPL_sci
    173. rh_IPL_sc
    174. rh_IPL_gr
    175. rh_IPL_gri
    176. rh_IPL_gci
    177. rh_IPL_gc
    178. rh_PrCu_vr
    179. rh_PrCu_dr
    180. rh_PrCu_dc
    181. rh_PrCu_di
    182. rh_PrCu_vi
    183. rh_PrCu_vc
    184. rh_PrL_d
    185. rh_PrL_i
    186. rh_PrL_STS
    187. rh_PrL_v
    188. rh_SFL_r
    189. rh_SFL_i
    190. rh_STG_gc
    191. rh_STG_gr
    192. rh_STG_gri
    193. rh_STG_gci
    194. rh_STSU_rEx
    195. rh_STSU_cEx
    196. rh_STSU_r
    197. rh_STSU_ri
    198. rh_STSU_ci
    199. rh_STSU_c
    200. rh_STSL_r
    201. rh_STSL_cIn
    202. rh_STSL_cEx
    203. rh_ITG_gr
    204. rh_ITG_gdc
    205. rh_ITG_gvc
    206. rh_PHG_r
    207. rh_PHG_mi
    208. rh_PHG_li
    209. rh_PHG_cm
    210. rh_PHG_cl
    211. rh_TP_vr
    212. rh_TP_mr
    213. rh_TP_lr
    214. rh_TP_dr
    215. rh_TP_cEx
    216. rh_TP_cIn
    217. rh_V1_cm
    218. rh_V1_dl
    219. rh_V1_vl
    220. rh_V1_mvi
    221. rh_V1_mdi
    222. rh_V1_rm
    223. rh_V2_l
    224. rh_V2_d
    225. rh_V2_v
    226. rh_V2_dm
    227. rh_V2_vm
    228. rh_VMO_l
    229. rh_VMO_i
    230. rh_VMO_m
    231. rh_INS_vr
    232. rh_INS_dr
    233. rh_INS_ri
    234. rh_INS_v
    235. rh_INS_ci
    236. rh_INS_c
    237. rh_CG_vr
    238. rh_CG_ir
    239. rh_CG_dr
    240. rh_CG_idr
    241. rh_CG_idc
    242. rh_CG_ivr
    243. rh_CG_ivc
    244. rh_CG_dc
    245. rh_CG_vc
    246. rh_CG_RSr
    247. rh_CG_RSi
    248. rh_CG_RSc

??? note "猕猴D99集所有脑区名字:"
    1. lh_8Bm
    2. lh_11l
    3. lh_14r
    4. lh_v23a
    5. lh_Ia
    6. lh_13b
    7. lh_36c
    8. lh_24a'
    9. lh_10mc
    10. lh_CPB
    11. lh_29
    12. lh_v23b
    13. lh_13l
    14. lh_V4
    15. lh_31
    16. lh_Ig
    17. lh_ML
    18. lh_23a
    19. lh_ER
    20. lh_10o
    21. lh_VIP
    22. lh_LIPv
    23. lh_8Bs
    24. lh_V1
    25. lh_G
    26. lh_9d
    27. lh_7op
    28. lh_V4t
    29. lh_46f
    30. lh_PE
    31. lh_TEav
    32. lh_32
    33. lh_AL
    34. lh_10mr
    35. lh_24b
    36. lh_1/2
    37. lh_8Av
    38. lh_ECL
    39. lh_FST
    40. lh_12m
    41. lh_V6Av
    42. lh_8Bd
    43. lh_TGvd
    44. lh_V3d
    45. lh_F1
    46. lh_Iam
    47. lh_SII
    48. lh_23b
    49. lh_13m
    50. lh_9m
    51. lh_EI
    52. lh_RPB
    53. lh_13a
    54. lh_AONd/m
    55. lh_F3
    56. lh_R
    57. lh_V6
    58. lh_TFO
    59. lh_V4v
    60. lh_46v
    61. lh_PEc
    62. lh_TGdd
    63. lh_35
    64. lh_A1
    65. lh_Ial
    66. lh_7m
    67. lh_v23b_question
    68. lh_23c
    69. lh_EC
    70. lh_Id
    71. lh_MIP
    72. lh_PIP
    73. lh_PFG/PF
    74. lh_TEpd
    75. lh_V3v
    76. lh_44
    77. lh_MT
    78. lh_TEm
    79. lh_Tpt
    80. lh_24c
    81. lh_MST
    82. lh_RM
    83. lh_STGr
    84. lh_Pi
    85. lh_F6
    86. lh_DP
    87. lh_12r
    88. lh_PrCO
    89. lh_PEci
    90. lh_TGdg
    91. lh_AIP
    92. lh_36p
    93. lh_LOP
    94. lh_11m
    95. lh_RTp
    96. lh_AONl
    97. lh_25
    98. lh_Pir
    99. lh_Iapm
    100. lh_RT
    101. lh_Opt/PG
    102. lh_TEpv
    103. lh_V3A
    104. lh_45a
    105. lh_TEO
    106. lh_F7
    107. lh_46d
    108. lh_Iai
    109. lh_F5
    110. lh_LIPd
    111. lh_V2
    112. lh_36r
    113. lh_12l
    114. lh_PEa
    115. lh_TGsts
    116. lh_RTM
    117. lh_3a/b
    118. lh_TGa
    119. lh_V6Ad
    120. lh_TF
    121. lh_45b
    122. lh_TEad
    123. lh_PGa
    124. lh_F4
    125. lh_8Ad
    126. lh_RTL
    127. lh_12o
    128. lh_CM
    129. lh_TAa
    130. lh_F2
    131. lh_TGvg
    132. lh_CL
    133. lh_TPO
    134. lh_TEa
    135. lh_IPa
    136. lh_ELr
    137. lh_ELc
    138. lh_V2_question
    139. lh_V2_or_v23b_question
    140. lh_30
    141. lh_24b'
    142. lh_24a
    143. lh_24c'
    144. lh_14c
    145. lh_TTv
    146. lh_EO
    147. lh_TH
    148. lh_Iapl
    149. lh_Ri
    150. rh_8Bm
    151. rh_11l
    152. rh_14r
    153. rh_v23a
    154. rh_Ia
    155. rh_13b
    156. rh_36c
    157. rh_24a'
    158. rh_10mc
    159. rh_CPB
    160. rh_29
    161. rh_v23b
    162. rh_13l
    163. rh_V4
    164. rh_31
    165. rh_Ig
    166. rh_ML
    167. rh_23a
    168. rh_ER
    169. rh_10o
    170. rh_VIP
    171. rh_LIPv
    172. rh_8Bs
    173. rh_V1
    174. rh_G
    175. rh_9d
    176. rh_7op
    177. rh_V4t
    178. rh_46f
    179. rh_PE
    180. rh_TEav
    181. rh_32
    182. rh_AL
    183. rh_10mr
    184. rh_24b
    185. rh_1/2
    186. rh_8Av
    187. rh_ECL
    188. rh_FST
    189. rh_12m
    190. rh_V6Av
    191. rh_8Bd
    192. rh_TGvd
    193. rh_V3d
    194. rh_F1
    195. rh_Iam
    196. rh_SII
    197. rh_23b
    198. rh_13m
    199. rh_9m
    200. rh_EI
    201. rh_RPB
    202. rh_13a
    203. rh_AONd/m
    204. rh_F3
    205. rh_R
    206. rh_V6
    207. rh_TFO
    208. rh_V4v
    209. rh_46v
    210. rh_PEc
    211. rh_TGdd
    212. rh_35
    213. rh_A1
    214. rh_Ial
    215. rh_7m
    216. rh_v23b_question
    217. rh_23c
    218. rh_EC
    219. rh_Id
    220. rh_MIP
    221. rh_PIP
    222. rh_PFG/PF
    223. rh_TEpd
    224. rh_V3v
    225. rh_44
    226. rh_MT
    227. rh_TEm
    228. rh_Tpt
    229. rh_24c
    230. rh_MST
    231. rh_RM
    232. rh_STGr
    233. rh_Pi
    234. rh_F6
    235. rh_DP
    236. rh_12r
    237. rh_PrCO
    238. rh_PEci
    239. rh_TGdg
    240. rh_AIP
    241. rh_36p
    242. rh_LOP
    243. rh_11m
    244. rh_RTp
    245. rh_AONl
    246. rh_25
    247. rh_Pir
    248. rh_Iapm
    249. rh_RT
    250. rh_Opt/PG
    251. rh_TEpv
    252. rh_V3A
    253. rh_45a
    254. rh_TEO
    255. rh_F7
    256. rh_46d
    257. rh_Iai
    258. rh_F5
    259. rh_LIPd
    260. rh_V2
    261. rh_36r
    262. rh_12l
    263. rh_PEa
    264. rh_TGsts
    265. rh_RTM
    266. rh_3a/b
    267. rh_TGa
    268. rh_V6Ad
    269. rh_TF
    270. rh_45b
    271. rh_TEad
    272. rh_PGa
    273. rh_F4
    274. rh_8Ad
    275. rh_RTL
    276. rh_12o
    277. rh_CM
    278. rh_TAa
    279. rh_F2
    280. rh_TGvg
    281. rh_CL
    282. rh_TPO
    283. rh_TEa
    284. rh_IPa
    285. rh_ELr
    286. rh_ELc
    287. rh_V2_question
    288. rh_V2_or_v23b_question
    289. rh_30
    290. rh_24b'
    291. rh_24a
    292. rh_24c'
    293. rh_14c
    294. rh_TTv
    295. rh_EO
    296. rh_TH
    297. rh_Iapl
    298. rh_Ri

??? note "黑猩猩BNA集所有脑区名字:"
    1. lh_SFG.r
    2. lh_SFG.ri
    3. lh_SFG.ci
    4. lh_SFG.c
    5. lh_SFG.lc
    6. lh_SFG.mc
    7. lh_MFG.r
    8. lh_MFG.ri
    9. lh_MFG.i
    10. lh_MFG.di
    11. lh_MFG.vi
    12. lh_MFG.dc
    13. lh_MFG.vc
    14. lh_IFG.r
    15. lh_IFG.ri
    16. lh_IFG.ci
    17. lh_IFG.dc
    18. lh_IFG.vc
    19. lh_IFG.c
    20. lh_OrG.m
    21. lh_OrG.r
    22. lh_OrG.i
    23. lh_OrG.c
    24. lh_OrG.rl
    25. lh_OrG.cl
    26. lh_PrG.rd
    27. lh_PrG.cd
    28. lh_PrG.ri
    29. lh_PrG.ci
    30. lh_PrG.i
    31. lh_PrG.vi
    32. lh_PrG.v
    33. lh_PCL.r
    34. lh_PCL.c
    35. lh_STG.r
    36. lh_STG.ri
    37. lh_STG.ci
    38. lh_STG.c
    39. lh_STG.dc
    40. lh_STG.vc
    41. lh_MTG.r
    42. lh_MTG.i
    43. lh_MTG.c
    44. lh_MTG.cv
    45. lh_ITG.r
    46. lh_ITG.dr
    47. lh_ITG.vr
    48. lh_ITG.i
    49. lh_ITG.dc
    50. lh_ITG.vc
    51. lh_ITG.c
    52. lh_FuG.r
    53. lh_FuG.ri
    54. lh_FuG.ci
    55. lh_FuG.m
    56. lh_FuG.lc
    57. lh_FuG.mc
    58. lh_PhG.r
    59. lh_PhG.mi
    60. lh_PhG.li
    61. lh_PhG.mc
    62. lh_PhG.lc
    63. lh_SPL.dr
    64. lh_SPL.vr
    65. lh_SPL.i
    66. lh_SPL.ci
    67. lh_SPL.c
    68. lh_IPL.r
    69. lh_IPL.ri
    70. lh_IPL.v
    71. lh_IPL.ci
    72. lh_IPL.c
    73. lh_PrL.r
    74. lh_PrL.c
    75. lh_Pcun.d
    76. lh_Pcun.di
    77. lh_Pcun.vi
    78. lh_Pcun.v
    79. lh_PoG.d
    80. lh_PoG.i
    81. lh_PoG.v
    82. lh_INS.dr
    83. lh_INS.ir
    84. lh_INS.vr
    85. lh_INS.rd
    86. lh_INS.cd
    87. lh_INS.i
    88. lh_INS.v
    89. lh_CG.r
    90. lh_CG.i
    91. lh_CG.dc
    92. lh_CG.vc
    93. lh_MVOcC.rd
    94. lh_MVOcC.cd
    95. lh_MVOcC.rv
    96. lh_MVOcC.cv
    97. lh_LOcC.d
    98. lh_LOcC.i
    99. lh_LOcC.rv
    100. lh_LOcC.cv
    101. rh_SFG.r
    102. rh_SFG.ri
    103. rh_SFG.ci
    104. rh_SFG.c
    105. rh_SFG.lc
    106. rh_SFG.mc
    107. rh_MFG.r
    108. rh_MFG.ri
    109. rh_MFG.i
    110. rh_MFG.di
    111. rh_MFG.vi
    112. rh_MFG.dc
    113. rh_MFG.vc
    114. rh_IFG.r
    115. rh_IFG.ri
    116. rh_IFG.ci
    117. rh_IFG.dc
    118. rh_IFG.vc
    119. rh_IFG.c
    120. rh_OrG.m
    121. rh_OrG.r
    122. rh_OrG.i
    123. rh_OrG.c
    124. rh_OrG.rl
    125. rh_OrG.cl
    126. rh_PrG.rd
    127. rh_PrG.cd
    128. rh_PrG.ri
    129. rh_PrG.ci
    130. rh_PrG.i
    131. rh_PrG.vi
    132. rh_PrG.v
    133. rh_PCL.r
    134. rh_PCL.c
    135. rh_STG.r
    136. rh_STG.ri
    137. rh_STG.ci
    138. rh_STG.c
    139. rh_STG.dc
    140. rh_STG.vc
    141. rh_MTG.r
    142. rh_MTG.i
    143. rh_MTG.c
    144. rh_MTG.cv
    145. rh_ITG.r
    146. rh_ITG.dr
    147. rh_ITG.vr
    148. rh_ITG.i
    149. rh_ITG.dc
    150. rh_ITG.vc
    151. rh_ITG.c
    152. rh_FuG.r
    153. rh_FuG.ri
    154. rh_FuG.ci
    155. rh_FuG.m
    156. rh_FuG.lc
    157. rh_FuG.mc
    158. rh_PhG.r
    159. rh_PhG.mi
    160. rh_PhG.li
    161. rh_PhG.mc
    162. rh_PhG.lc
    163. rh_SPL.dr
    164. rh_SPL.vr
    165. rh_SPL.i
    166. rh_SPL.ci
    167. rh_SPL.c
    168. rh_IPL.r
    169. rh_IPL.ri
    170. rh_IPL.v
    171. rh_IPL.ci
    172. rh_IPL.c
    173. rh_PrL.r
    174. rh_PrL.c
    175. rh_Pcun.d
    176. rh_Pcun.di
    177. rh_Pcun.vi
    178. rh_Pcun.v
    179. rh_PoG.d
    180. rh_PoG.i
    181. rh_PoG.v
    182. rh_INS.dr
    183. rh_INS.ir
    184. rh_INS.vr
    185. rh_INS.rd
    186. rh_INS.cd
    187. rh_INS.i
    188. rh_INS.v
    189. rh_CG.r
    190. rh_CG.i
    191. rh_CG.dc
    192. rh_CG.vc
    193. rh_MVOcC.rd
    194. rh_MVOcC.cd
    195. rh_MVOcC.rv
    196. rh_MVOcC.cv
    197. rh_LOcC.d
    198. rh_LOcC.i
    199. rh_LOcC.rv
    200. rh_LOcC.cv

!!! warning
    画图时请保证脑区名字正确。


```python
from plotfig import *

data = {"lh_V1": 1, "rh_MT": 1.5}

fig = plot_human_brain_figure(data)
```


    
![png](brain_surface_files/brain_surface_12_0.png)
    


同样还可以绘制猕猴和黑猩猩的图像。


```python
from plotfig import *

macaque_data = {"lh_V1": 1}
chimpanzee_data = {"lh_MVOcC.rv": 1}

fig = plot_macaque_brain_figure(macaque_data, title_name="Macaque")
fig = plot_chimpanzee_brain_figure(chimpanzee_data, title_name="Chimpanzee")
```


    
![png](brain_surface_files/brain_surface_14_0.png)
    



    
![png](brain_surface_files/brain_surface_14_1.png)
    


### 参数设置

全部参数见[`plotfig.brain_surface`](../api/index.md/#plotfig.brain_surface)的API 文档。

!!! note
    人/黑猩猩/猕猴脑区图绘制参数相同，只是函数名称以及图集名称不同。


我们可以选择真实沟回surface作为underlay图。
同时选择`surfplot` api自带的colorbar (功能相对较少)。


```python
from plotfig import *

data = {"lh_V1": 1, "rh_MT": 1.5, "rh_V1": -1}

fig = plot_human_brain_figure(
    data,
    surf="midthickness",
    atlas="glasser",
    cmap="bwr",
    vmin=-1,
    vmax=1,
    colorbar=True,
    colorbar_label_name="A",
    colorbar_fontsize=10,
    colorbar_nticks=4,
    colorbar_shrink=0.2,
    colorbar_location="right",
    colorbar_draw_border=True,
)

```


    
![png](brain_surface_files/brain_surface_17_0.png)
    


也可以使用自定义功能更多的`rjx_colorbar`。

!!! warning
    使用`rjx_colorbar`时请确保`colorbar`为`False`。


```python
from plotfig import *

data = {"lh_V1": 1, "rh_MT": 1.5, "rh_V1": -1}

fig = plot_human_brain_figure(
    data,
    surf="inflated",
    atlas="glasser",
    cmap="viridis",
    vmin=-1,
    vmax=1,
    colorbar=False,
    rjx_colorbar=True,
    rjx_colorbar_direction="vertical",
    rjx_colorbar_label_name="A",
    rjx_colorbar_tick_length=3,
    rjx_colorbar_label_fontsize=15,
    rjx_colorbar_tick_fontsize=10,
    rjx_colorbar_outline=True,
    rjx_colorbar_nticks=2
)

```


    
![png](brain_surface_files/brain_surface_19_0.png)
    


`rjx_colorbar`还允许水平方向的colorbar，更加节省图片空间。


```python
from plotfig import *

data = {"lh_V1": 1, "rh_MT": 1.5, "rh_V1": -1}

fig = plot_macaque_brain_figure(
    data,
    surf="veryinflated",
    atlas="charm5",
    cmap="viridis",
    vmin=-1,
    vmax=1,
    colorbar=False,
    rjx_colorbar=True,
    rjx_colorbar_direction="horizontal",
    rjx_colorbar_label_name="A",
    rjx_colorbar_tick_length=3,
    rjx_colorbar_label_fontsize=15,
    rjx_colorbar_tick_fontsize=10,
    rjx_colorbar_outline=True,
    rjx_colorbar_nticks=3
)

```


    
![png](brain_surface_files/brain_surface_21_0.png)
    


## 半脑

有时我们只希望展示半边大脑。

!!! note
    绘制半脑的函数参数与全脑基本相同。但是多了一个`hemi`来指定绘制的半边，且仅有普通的`colorbar`，而没有`rjx_colorbar`。
    需要强调的是，绘制左脑，请保证脑区名字为“lh_”开头，同理，绘制右脑，请保证脑区名字为“rh_”开头。


```python
from plotfig import *

data = {"lh_V1": 1}

fig = plot_human_hemi_brain_figure(
    data,
    hemi="lh",
    title_name="Left brain V1"
)
```


    
![png](brain_surface_files/brain_surface_24_0.png)
    



```python
from plotfig import *

data = {"rh_V1": 1}

fig = plot_human_hemi_brain_figure(
    data,
    hemi="rh",
    title_name="Right brain V1",
    colorbar=True,
    colorbar_label_name="A",
    colorbar_aspect=8,
    colorbar_fontsize=10,
    colorbar_nticks=4,
    colorbar_decimals=3
)
```


    
![png](brain_surface_files/brain_surface_25_0.png)
    

