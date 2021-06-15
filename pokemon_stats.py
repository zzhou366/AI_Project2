
"""
Created on Sat Nov  7 14:56:08 2020

@author: Tony Zhou
"""
import csv
import numpy as np
import math
import ast
from scipy.cluster.hierarchy import dendrogram, linkage

# =============================================================================
# this method help to create a list of dictionaries containing data from row 1 
# to row 20
# =============================================================================
def load_data(filepath):
    pokemon_data = []
    dict_key = []
    # with open(filepath, 'r') as csvfile:
    with open(filepath, 'r', encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        linecount = 0
        for row in csvreader:
        
            
            if linecount == 0:
                for i in range(len(row) - 2):
                    dict_key.append(row[i])
                linecount += 1
                
            else:
                if linecount < 21:
                    data = {}
                  
          
                    for i in range(len(row) - 2):
                        if i <= 3:
                            if i == 0:
                                data[dict_key[i]] = int(row[i])
                            else:
                                data[dict_key[i]] = row[i]
                        else:
                            data[dict_key[i]] = int(row[i])
                            
                            
               
                            
                        
                    pokemon_data.append(data)
                    linecount += 1
                    
                    
                else:
                    break
 
    
        
                
    return pokemon_data


def calculate_x_y(stats):
    x = int(stats['Attack']) + int(stats['Sp. Atk']) + int(stats['Speed'])
    y = int(stats['Defense']) + int(stats['Sp. Def']) + int(stats['HP'])

    return (x,y)
   

def getDistance(A,B):
    return math.sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )

 

#merge two subclusters into a new cluster
def merge(A,B):
    cluster = []

    
    # make sure A and B are not string
    
    A = ast.literal_eval(A)
    B = ast.literal_eval(B)
    
    if (type(A) == tuple) and (type(B) == tuple):

        cluster.append(A)
        cluster.append(B)

        return cluster
        
    
    else:
        if type(A) == list:
            cluster = A
            if type(B) == list:
                for i in B:
                    cluster.append(i)
           
                return cluster
            else:
                cluster.append(B)
           
                return cluster
        if type(B) == list:
                 cluster = B
                 if type(A) == list:
                     for j in A:
                         cluster.append(j)
           
                     return cluster
                 else:
                     cluster.append(A)
       
                     return cluster
  

def contruct_distance_ds(dataset):

    original_distance_ds = {}# track the original clusters distance between each others
    original_indices_ds = {}# track the indices of original clusters
    
    index = 0
    for starter in dataset:
        original_indices_ds[str(starter)] = index
 
        index += 1
        for end in dataset:
            original_distance_ds[str(starter)+'-'+str(end)] = getDistance(starter, end)


    return original_distance_ds, original_indices_ds

#update the distance table base on new dataset
def updat_distance_ds(dataset, original_distance_ds):
    update_dis_table = {}

    for starter in dataset:
        # if the current position is a tuple 
        # (a)
        if type(starter) == tuple:
            for end in dataset:
                 #check if the current position is a tuple 
                if type(end) == tuple:
                    update_dis_table[str(starter)+'-'+str(end)] = original_distance_ds[str(starter)+'-'+str(end)]
                else:
                    #D(a,(b,c)) = MIN(D(a,b), D(a,c))
                    pick_min_dis = []
                    for element in end:
                        pick_min_dis.append(original_distance_ds[str(starter)+'-'+str(element)])
                    update_dis_table[str(starter)+'-'+str(end)] = min(pick_min_dis)
        # if the current position is a list
        # (a,b)
        else:
            for i in dataset:
                # if identical then their distance is 0
                if i == starter:
                    update_dis_table[str(starter)+'-'+str(i)] = 0
                    continue
                # if i is a tuple
                if type(i) == tuple:
                    a = []
                    for j in starter:
                        a.append(original_distance_ds[str(j)+'-'+str(i)])
                    update_dis_table[str(starter)+'-'+str(i)] = min(a)
                    continue
                # when two cluster with more than one points meet
                # D((a,b),(c,d)) = MIN(D(a,c),D(a,d),D(b,c),D(b,d))
                if type(i) == list:
                    b = []
                    for p in starter:
                        for q in i:
                            b.append(original_distance_ds[str(p)+'-'+str(q)])
                    update_dis_table[str(starter)+'-'+str(i)] = min(b)
                    

    
                    
    return update_dis_table    
                               
        

    
        
def get_nums_merging_point(mergePoints):

    nums = 0
    for element in mergePoints:
        a = ast.literal_eval(element)
        # element is a single tuple
        if type(a) == tuple:
            nums += 1
            continue
        if type(a) == list:
            for item in a:
                nums += 1
 
    
    return nums
        
            
    
    
        
def hac(dataset1):
    
    
    dataset = dataset1[:]
  

    haclog = []# the future numpy array we will return in the end
    
    # aquire the original distance table and indices table
    oringinal_dis_table, ind_table = contruct_distance_ds(dataset)
    # print(oringinal_dis_table)
    
    
    
    dis_table = oringinal_dis_table
    # Start clustering until there is only one cluster left
    roundcount = 0
    while len(dataset) > 1:
 
        roundcount+=1
     
        #update the current loop distance list to find the closest distance
        loop_dis_list = []
        for i in dis_table:
            if dis_table[i] != 0:
                loop_dis_list.append(dis_table[i])
        loop_dis_list.sort()        
 
        
        #tie breaking
        #aquire the smallest distance, append their makers into a list for future tie-breaking
        if roundcount == 19:
              print(loop_dis_list)
            
        tie_breaking_dapoint = []
        for b in dis_table:
            
         
        
            if dis_table[b] == loop_dis_list[0]:
                tie_breaking_dapoint.append(b)
        tie_breaking_dapoint = tie_breaker(tie_breaking_dapoint,ind_table)
 
        loop_merge_points = tie_breaking_dapoint[0].split('-')

        loop_merge_indicies = []
        for c in loop_merge_points:
            loop_merge_indicies.append(ind_table[c])
 
        loop_distance = loop_dis_list[0]
        
        #count how many points got merged this time
        loop_nums_points = get_nums_merging_point(loop_merge_points)
        
        single_log = [loop_merge_indicies[0],loop_merge_indicies[1],loop_distance,loop_nums_points]
        haclog.append(single_log)
      
        
        #merge and update the ind_table, dis_table
        mergeCluster = merge(loop_merge_points[0], loop_merge_points[1])

        dataset.append(mergeCluster)
        ind_table[str(mergeCluster)] = len(ind_table)

        dataset.remove(ast.literal_eval(loop_merge_points[0]))
        dataset.remove(ast.literal_eval(loop_merge_points[1]))
   
        dis_table = updat_distance_ds(dataset, oringinal_dis_table)

    
    haclog = np.array(haclog)
        
         
    return haclog


            
    
def tie_breaker(datalist,ind_table):

    return datalist
    

    
    
    
    
    





