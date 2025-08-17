'''
PART 2: NETWORK CENTRALITY METRICS

Using the imbd_movies dataset
- Build a graph and perform some rudimentary graph analysis, extracting centrality metrics from it. 
- Below is some basic code scaffolding that you will need to add to
- Tailor this code scaffolding and its stucture to however works to answer the problem
- Make sure the code is inline with the standards we're using in this class 
'''

import numpy as np
import pandas as pd
import networkx as nx
import json
import datetime as dt

def nc():
    """
    Creates a graph that connects actors with eachother based on movie apperances 
    Args: 
        none
    Returns: 
        Saves a CSV to 'data/'
    """
    
    # Creates graph
    g = nx.Graph()
    
    # Reads in json file
    with open('data/data.json', 'r') as in_file:
        for line in in_file:

            # Load the movie from this line
            this_movie = json.loads(line)
                
            # Creates a node for every actor and adds the actor to the graph
            for actor_id,actor_name in this_movie['actors']:
                g.add_node(actor_id, name= actor_name)
            
            i = 0 #counter
            for left_actor_id,left_actor_name in this_movie['actors']:
                for right_actor_id,right_actor_name in this_movie['actors'][i+1:]:
                    
                     # Get the current weight, if it exists
                    if g.has_edge(left_actor_id, right_actor_id):
                        current_edge = g[left_actor_id][right_actor_id]
                        current_weight = current_edge['weight']
                    else:
                        current_weight = 0
                    
                     # Add an edge between left and right actor
                    g.add_edge(left_actor_id, right_actor_id, weight= current_weight + 1)
                    i += 1

    print("Nodes:", len(g.nodes))

    # Gets degree of centrality 
    deg_cent = nx.degree_centrality(g)

    # Creates a df for actor centrality
    centrality_data = []
    for node_id in g.nodes():
        node_name = g.nodes[node_id]['name']
        centrality_data.append({
            'actor_id': node_id,
            'actor_name': node_name,
            'degree_centrality': deg_cent[node_id]
        })

    centrality_df = pd.DataFrame(centrality_data)
    centrality_df = centrality_df.sort_values('degree_centrality', ascending=False)

    print('10 most central nodes:')
    print(centrality_df[['actor_name', 'degree_centrality']].head(10))

    # Saves centrality_df to 'data/'
    current_dt = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    centrality_df.to_csv(f'data/network_centrality_{current_dt}.csv')

