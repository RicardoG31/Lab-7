# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:52:22 2018

@author: Ricardo
"""
# Course: CS2302
# Author: Ricardo Godoy
# Assignment: Lab 7
# T.A: Saha, Manoj
# Instructor: Diego Aguirre
# Date of last modification: 11/27/18

#The purpose of this lab is to implement Dynamic Programming to find the number of modifications
#necessary for string 2 (s2) to be the same as string 1 (s1)

def read(filename):#This function reads the file containing the strings and appends them into a list
    strings = []
    file = open(filename)
    for line in file:
        string = line.replace("\n", "")
        strings.append(string)
    return strings


def edit_distance(strings):#This function creates a matrix and computes the number of modifications necessary for the strings to be the same
    s1 = strings[0]
    s2 = strings[1]
    matrix = [[0] * (len(s2)) for i in range(len(s1))]
    print("Edit distance on strings: " + s1 + " and " + s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                matrix[i][j] = matrix[i-1][j-1]
                
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
    changes = matrix[len(s1)-1][len(s2)-1] 
    print("Changes needed : ", changes)
    print("Matrix: \n", matrix)
    
    
    
    
    
def main():
    filename = "Strings.txt"
    strings = read(filename)
    edit_distance(strings)
main()
        