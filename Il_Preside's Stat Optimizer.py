#Hello, I will provide a very basic description of how to use this script.
# 
#First of all, you are required to have different armor pieces in order to have a significant amount of armor combinations.
# 
#Second of all, there will be 4 matrices you have to compile. H represents Helmets, G is for Gloves, C is for Chestpieces and L is for Legpieces. These four matrices follow the same syntax.
#
#----------------------------------------------------------------------------------------------------READ ME----------------------------------------------------------------------------------------------------
#
#Let's say your Helmet has 12 Mobility, 10 Resilience, 6 Recovery, 10 Discipline, 2 Intellect and 10 Strength. The correct way to type in the numbers is as follows:
# 
#H = [[12, 10, 6, 10, 2, 10]]
# 
#If you want to use at least two Helmets you have to separate each vector using a comma, like the following example:
# 
#H = [[12, 10, 6, 10, 2, 10], [13, 5, 5, 6, 18, 17]]
# 
#The same is also true for the matrices of Gloves, Chestpieces and Legpieces. They function the same way:
#
#G = [[a, b, c, d, e, f], [g, h, j, k, l, m]]
# 
#C = [[a, b, c, d, e, f], [g, h, j, k, l, m]]
# 
#L = [[a, b, c, d, e, f], [g, h, j, k, l, m]]
# 
#Now that you know the syntax you can start using the program by choosing the Exotic piece you desire. If you have multiple copies of the same exotic, type them all in the correct matrix.
# 
#After the Exotic piece(s), you have to fill the other matrices by following the syntax above.
#
#I will provide a template of the four matrices that I used in the example image. As you can see, G (Gloves) only has one element because I want Synthoceps specifically and I only have one.
#
#----------------------------------------------------------------------------------------------------INPUTS----------------------------------------------------------------------------------------------------

H = [[6, 10, 16, 18, 2, 12],
     [11, 2, 20, 12, 12, 9],
     [8, 10, 14, 11, 14, 6],
     [15, 2, 14, 7, 18, 6],
     [2, 15, 15, 16, 16, 2]]

G = [[11, 8, 12, 7, 7, 15]]

C = [[10, 7, 16, 18, 7, 10],
     [10, 12, 11, 16, 9, 7],
     [2, 12, 17, 14, 7, 12],
     [7, 15, 10, 15, 7, 8],
     [12, 2, 18, 11, 10, 10],
     [12, 2, 16, 11, 17, 2]]

L = [[10, 6, 17, 10, 12, 11],
     [15, 6, 12, 12, 10, 10],
     [7, 6, 20, 12, 9, 12],
     [2, 8, 19, 15, 14, 2],
     [2, 13, 14, 13, 2, 15],
     [2, 10, 18, 12, 10, 6],
     [2, 19, 10, 12, 2, 19]]

#--------------------------------------------------------------------------------------------------END INPUTS--------------------------------------------------------------------------------------------------
#
#Replace my elements with yours, then go in the top left corner. Click FILE, then SAVE. This will allow you to store your values in this file.
#
#Lastly, go in the top left corner again, click RUN, then RUN MODULE. A tab will open.
# 
#After all four of the matrices are full you can operate the program by typing one of three functions:
# 
#1) Filter(H, G, C, L, MOBmin, MOBmax, RESmin, RESmax, RECmin, RECmax, DISCmin, DISCmax, INTmin, INTmax, STRmin, STRmax)
# 
#As I mentioned above, the matrices H, G, C and L are now in your memory, therefore you must not change the letters inside the round brackets.
# 
#The values of MOBmin and MOBmax represent the minimum and the maximum value of Mobility that you want to have, respectively.
# 
#If you want at least 30 Mobility but no more than 50 you have to delete MOBmin and replace it with 30, then delete MOBmax and replace it with 50 in the Filter function.
# 
#This is also true for the other stats, therefore if you don't have any conditions to apply to them you have to type 0 in the minimum and 100 in the maximum.
# 
#The output of the following example is a list of all the armor combinations that follow your restrictions, in this case 30 < Mobility < 50 :
# 
#Filter(H, G, C, L, 30, 50, 0, 100, 0, 100, 0, 100, 0, 100, 0, 100)
# 
#Make sure the conditions are reasonable because, if you are too strict, no matches will be found.
# 
#2) Minimize(H, G, C, L, diffzero) where diffzero is a number that represents the total amount of points wasted. 21 Resilience and 42 Discipline imply a waste of 3 total points, so you have to replace diffzero with a low number.
# 
#I personally recommend to start from diffzero around 15. If you see too many combinations, you can copy-paste the Minimize function and lower that value so that the script will filter the most optimal combinations.
#
#Minimize(H, G, C, L, 15)
#
#3) MaxTier(H, G, C, L, tierzero) where tierzero is a number that represents the minimum Tier you desire. If you want an armor combinations that is Tier 23 or above, just replace tierzero with 23.
#
#I personally recommend starting around 24. Builds that are lower than this usually are not optimal. If you see no results, lower the variable tierzero.
#
#MaxTier(H, G, C, L, 23)
#
#
#
#
#
#
#
#----------------------------------------------------------------------------------------------------SCRIPT BEGINS----------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#

def filter(H, G, C, L, MOBmin, MOBmax, RESmin, RESmax, RECmin, RECmax, DISCmin, DISCmax, INTmin, INTmax, STRmin, STRmax):
    
    import numpy
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    rowsH = numpy.shape(H)[0]
    rowsG = numpy.shape(G)[0]
    rowsC = numpy.shape(C)[0]
    rowsL = numpy.shape(L)[0]

    R = ([])

    print(" ")
    print("-----------------------------------------------------")
    print(" ")

    while a<(rowsH - 0.5):

        while b<(rowsG - 0.5):

            while c<(rowsC - 0.5):

                while d<(rowsL - 0.5):

                    stat0 = H[a][0]+G[b][0]+C[c][0]+L[d][0]
                    stat1 = H[a][1]+G[b][1]+C[c][1]+L[d][1]
                    stat2 = H[a][2]+G[b][2]+C[c][2]+L[d][2]
                    stat3 = H[a][3]+G[b][3]+C[c][3]+L[d][3]
                    stat4 = H[a][4]+G[b][4]+C[c][4]+L[d][4]
                    stat5 = H[a][5]+G[b][5]+C[c][5]+L[d][5]

                    mobtier = (H[a][0]+G[b][0]+C[c][0]+L[d][0])//10
                    restier = (H[a][1]+G[b][1]+C[c][1]+L[d][1])//10
                    rectier = (H[a][2]+G[b][2]+C[c][2]+L[d][2])//10
                    disctier = (H[a][3]+G[b][3]+C[c][3]+L[d][3])//10
                    inttier = (H[a][4]+G[b][4]+C[c][4]+L[d][4])//10
                    strtier = (H[a][5]+G[b][5]+C[c][5]+L[d][5])//10

                    tier = mobtier + restier + rectier + disctier + inttier + strtier

                    diffcheck = stat0+stat1+stat2+stat3+stat4+stat5 - 10*tier

                    if H[a][0]+G[b][0]+C[c][0]+L[d][0]>=MOBmin:
                        if H[a][0]+G[b][0]+C[c][0]+L[d][0]<=MOBmax:
                            if H[a][1]+G[b][1]+C[c][1]+L[d][1]>=RESmin:
                                if H[a][1]+G[b][1]+C[c][1]+L[d][1]<=RESmax:
                                    if H[a][2]+G[b][2]+C[c][2]+L[d][2]>=RECmin:
                                        if H[a][2]+G[b][2]+C[c][2]+L[d][2]<=RECmax:
                                            if H[a][3]+G[b][3]+C[c][3]+L[d][3]>=DISCmin:
                                                if H[a][3]+G[b][3]+C[c][3]+L[d][3]<=DISCmax:
                                                    if H[a][4]+G[b][4]+C[c][4]+L[d][4]>=INTmin:
                                                        if H[a][4]+G[b][4]+C[c][4]+L[d][4]<=INTmax:
                                                            if H[a][5]+G[b][5]+C[c][5]+L[d][5]>=STRmin:
                                                                if H[a][5]+G[b][5]+C[c][5]+L[d][5]<=STRmax:
                                                                    
                                                                    R.append([H[a][0]+G[b][0]+C[c][0]+L[d][0], H[a][1]+G[b][1]+C[c][1]+L[d][1], H[a][2]+G[b][2]+C[c][2]+L[d][2], H[a][3]+G[b][3]+C[c][3]+L[d][3], H[a][4]+G[b][4]+C[c][4]+L[d][4], H[a][5]+G[b][5]+C[c][5]+L[d][5]])

                                                                    #This is the sum of Mobility stats. ^      This is Resilience. ^            This is Recovery. ^              This is Discipline. ^            This is Intellect. ^             This is Strength. ^

                                                                    print("GLOBAL STATS =========", [H[a][0]+G[b][0]+C[c][0]+L[d][0], H[a][1]+G[b][1]+C[c][1]+L[d][1], H[a][2]+G[b][2]+C[c][2]+L[d][2], H[a][3]+G[b][3]+C[c][3]+L[d][3], H[a][4]+G[b][4]+C[c][4]+L[d][4], H[a][5]+G[b][5]+C[c][5]+L[d][5]])
                                                                    print(" ")
                                                                    print("TOTAL TIER LEVEL =====", tier, "BASE ----->", tier+6, "FULLY MASTERWORKED")
                                                                    print(" ")
                                                                    print("WASTED POINTS ========", diffcheck)             
                                                                    print(" ")
                                                                    print("HELMET STATS =========", [H[a][0], H[a][1], H[a][2], H[a][3], H[a][4], H[a][5]])
                                                                    print(" ")
                                                                    print("GLOVE STATS ==========", [G[b][0], G[b][1], G[b][2], G[b][3], G[b][4], G[b][5]])
                                                                    print(" ")
                                                                    print("CHESTPIECE STATS =====", [C[c][0], C[c][1], C[c][2], C[c][3], C[c][4], C[c][5]])
                                                                    print(" ")
                                                                    print("LEGPIECE STATS =======", [L[d][0], L[d][1], L[d][2], L[d][3], L[d][4], L[d][5]])
                                                                    print(" ")
                                                                    print(" ")
                                                                    print("---------------------------------------------------------------")
                                                                    print(" ")
                                                                    print(" ")
                                                                    
                                                                    f = f+1

                    d = d+1
                    e = e+1

                c = c+1
                d = 0

            b = b+1
            c = 0
            d = 0

        a = a+1
        b = 0
        c = 0
        d = 0

    print("Total combinations =", e)
    print(" ")
    print("---------------------------------------------------------------")
    print(" ")
    print("Total combinations that follow your filter =", f)
    print(" ")

def minimize(H, G, C, L, diffzero):
    
    import numpy
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    rowsH = numpy.shape(H)[0]
    rowsG = numpy.shape(G)[0]
    rowsC = numpy.shape(C)[0]
    rowsL = numpy.shape(L)[0]

    K = ([])

    print(" ")
    print("-----------------------------------------------------")
    print(" ")
    
    while a<(rowsH - 0.5):

        while b<(rowsG - 0.5):

            while c<(rowsC - 0.5):

                while d<(rowsL - 0.5):
                    
                    stat0 = H[a][0]+G[b][0]+C[c][0]+L[d][0]
                    stat1 = H[a][1]+G[b][1]+C[c][1]+L[d][1]
                    stat2 = H[a][2]+G[b][2]+C[c][2]+L[d][2]
                    stat3 = H[a][3]+G[b][3]+C[c][3]+L[d][3]
                    stat4 = H[a][4]+G[b][4]+C[c][4]+L[d][4]
                    stat5 = H[a][5]+G[b][5]+C[c][5]+L[d][5]

                    ten0 = (H[a][0]+G[b][0]+C[c][0]+L[d][0])//10
                    ten1 = (H[a][1]+G[b][1]+C[c][1]+L[d][1])//10
                    ten2 = (H[a][2]+G[b][2]+C[c][2]+L[d][2])//10
                    ten3 = (H[a][3]+G[b][3]+C[c][3]+L[d][3])//10
                    ten4 = (H[a][4]+G[b][4]+C[c][4]+L[d][4])//10
                    ten5 = (H[a][5]+G[b][5]+C[c][5]+L[d][5])//10

                    diffcheck = stat0+stat1+stat2+stat3+stat4+stat5 - 10*(ten0+ten1+ten2+ten3+ten4+ten5)
                    
                    if diffcheck <= diffzero:
                        
                        K.append([H[a][0]+G[b][0]+C[c][0]+L[d][0], H[a][1]+G[b][1]+C[c][1]+L[d][1], H[a][2]+G[b][2]+C[c][2]+L[d][2], H[a][3]+G[b][3]+C[c][3]+L[d][3], H[a][4]+G[b][4]+C[c][4]+L[d][4], H[a][5]+G[b][5]+C[c][5]+L[d][5]])

                        #This is the sum of Mobility stats. ^      This is Resilience. ^            This is Recovery. ^              This is Discipline. ^            This is Intellect. ^             This is Strength. ^

                        print("GLOBAL STATS =========", [H[a][0]+G[b][0]+C[c][0]+L[d][0], H[a][1]+G[b][1]+C[c][1]+L[d][1], H[a][2]+G[b][2]+C[c][2]+L[d][2], H[a][3]+G[b][3]+C[c][3]+L[d][3], H[a][4]+G[b][4]+C[c][4]+L[d][4], H[a][5]+G[b][5]+C[c][5]+L[d][5]])
                        print(" ")
                        print("TOTAL TIER LEVEL =====", ten0+ten1+ten2+ten3+ten4+ten5, "BASE ----->", ten0+ten1+ten2+ten3+ten4+ten5+6, "FULLY MASTERWORKED")
                        print(" ")
                        print("WASTED POINTS ========", diffcheck)             
                        print(" ")
                        print("HELMET STATS =========", [H[a][0], H[a][1], H[a][2], H[a][3], H[a][4], H[a][5]])
                        print(" ")
                        print("GLOVE STATS ==========", [G[b][0], G[b][1], G[b][2], G[b][3], G[b][4], G[b][5]])
                        print(" ")
                        print("CHESTPIECE STATS =====", [C[c][0], C[c][1], C[c][2], C[c][3], C[c][4], C[c][5]])
                        print(" ")
                        print("LEGPIECE STATS =======", [L[d][0], L[d][1], L[d][2], L[d][3], L[d][4], L[d][5]])
                        print(" ")
                        print("---------------------------------------------------------------")
                        print(" ")
                        print(" ")

                        f = f+1

                    d = d+1
                    e = e+1

                c = c+1
                d = 0

            b = b+1
            c = 0
            d = 0

        a = a+1
        b = 0
        c = 0
        d = 0

    print("Total combinations =", e)
    print(" ")
    print("-----------------------------------------------------")
    print(" ")
    print("Total combinations that follow your filter =", f)
    print(" ")

def maxtier(H, G, C, L, tierzero):
    
    import numpy
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0

    rowsH = numpy.shape(H)[0]
    rowsG = numpy.shape(G)[0]
    rowsC = numpy.shape(C)[0]
    rowsL = numpy.shape(L)[0]

    B = ([])

    print(" ")
    print("-----------------------------------------------------")
    print(" ")
    
    while a<(rowsH - 0.5):

        while b<(rowsG - 0.5):

            while c<(rowsC - 0.5):

                while d<(rowsL - 0.5):
                    
                    stat0 = H[a][0]+G[b][0]+C[c][0]+L[d][0]
                    stat1 = H[a][1]+G[b][1]+C[c][1]+L[d][1]
                    stat2 = H[a][2]+G[b][2]+C[c][2]+L[d][2]
                    stat3 = H[a][3]+G[b][3]+C[c][3]+L[d][3]
                    stat4 = H[a][4]+G[b][4]+C[c][4]+L[d][4]
                    stat5 = H[a][5]+G[b][5]+C[c][5]+L[d][5]

                    mobtier = (H[a][0]+G[b][0]+C[c][0]+L[d][0])//10
                    restier = (H[a][1]+G[b][1]+C[c][1]+L[d][1])//10
                    rectier = (H[a][2]+G[b][2]+C[c][2]+L[d][2])//10
                    disctier = (H[a][3]+G[b][3]+C[c][3]+L[d][3])//10
                    inttier = (H[a][4]+G[b][4]+C[c][4]+L[d][4])//10
                    strtier = (H[a][5]+G[b][5]+C[c][5]+L[d][5])//10

                    tier = mobtier + restier + rectier + disctier + inttier + strtier

                    diffcheck = stat0+stat1+stat2+stat3+stat4+stat5 - 10*tier 
                    
                    if tier >= tierzero:
                        
                        B.append([H[a][0]+G[b][0]+C[c][0]+L[d][0], H[a][1]+G[b][1]+C[c][1]+L[d][1], H[a][2]+G[b][2]+C[c][2]+L[d][2], H[a][3]+G[b][3]+C[c][3]+L[d][3], H[a][4]+G[b][4]+C[c][4]+L[d][4], H[a][5]+G[b][5]+C[c][5]+L[d][5]])

                        #This is the sum of Mobility stats. ^      This is Resilience. ^            This is Recovery. ^              This is Discipline. ^            This is Intellect. ^             This is Strength. ^

                        print("GLOBAL STATS =========", [H[a][0]+G[b][0]+C[c][0]+L[d][0], H[a][1]+G[b][1]+C[c][1]+L[d][1], H[a][2]+G[b][2]+C[c][2]+L[d][2], H[a][3]+G[b][3]+C[c][3]+L[d][3], H[a][4]+G[b][4]+C[c][4]+L[d][4], H[a][5]+G[b][5]+C[c][5]+L[d][5]])
                        print(" ")
                        print("TOTAL TIER LEVEL =====", tier, "BASE ----->", tier+6, "FULLY MASTERWORKED")
                        print(" ")
                        print("WASTED POINTS ========", diffcheck)             
                        print(" ")
                        print("HELMET STATS =========", [H[a][0], H[a][1], H[a][2], H[a][3], H[a][4], H[a][5]])
                        print(" ")
                        print("GLOVE STATS ==========", [G[b][0], G[b][1], G[b][2], G[b][3], G[b][4], G[b][5]])
                        print(" ")
                        print("CHESTPIECE STATS =====", [C[c][0], C[c][1], C[c][2], C[c][3], C[c][4], C[c][5]])
                        print(" ")
                        print("LEGPIECE STATS =======", [L[d][0], L[d][1], L[d][2], L[d][3], L[d][4], L[d][5]])
                        print(" ")
                        print(" ")
                        print("---------------------------------------------------------------")
                        print(" ")
                        print(" ")

                        f = f+1

                    d = d+1
                    e = e+1

                c = c+1
                d = 0

            b = b+1
            c = 0
            d = 0

        a = a+1
        b = 0
        c = 0
        d = 0

    print("Total combinations =", e)
    print(" ")
    print("-----------------------------------------------------")
    print(" ")
    print("Total combinations that follow your filter =", f)
    print(" ")
    
#
#
#
#
#
#
#
#----------------------------------------------------------------------------------------------------SCRIPT ENDS----------------------------------------------------------------------------------------------------
#
#
#
#
#
#
#
