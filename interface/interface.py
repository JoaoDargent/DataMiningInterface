import streamlit as st
import os
import pandas as pd
import pickle
import plotly.express as px

# Create sidebar navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['About Us', 'EDA Raw Data', 'Segmentation & Clustering', 'Final Clusterization'])

# About Us page
if page == 'About Us':
    st.title('About Us')
    st.write('Welcome to our data analysis application. We help you understand and segment your data.')
    
    if st.button('Learn More'):
        st.write('We are a team of data scientists passionate about finding insights in data.')

# EDA (Exploratory Data Analysis) page        
elif page == 'EDA Raw Data':
    st.title('Exploratory Data Analysis')
    st.write('Upload your data and explore key insights through visualizations and statistics.')
    
    # Update the path to use interface/plots
    plot_directory = 'interface/plots/rawData/Distributions'
    
    try:
        # Check if directory exists
        if not os.path.exists(plot_directory):
            st.error(f"Directory not found: {plot_directory}")
            st.info("Please make sure the plots directory is properly set up.")
        else:
            plot_options = [f for f in os.listdir(plot_directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
            
            # Check if there are any plot options available
            if plot_options:
                # Remove the file extensions for the selectbox options
                plot_options_no_ext = [os.path.splitext(f)[0] for f in plot_options]
                
                # Dropdown menu to select a plot
                selected_plot = st.selectbox('Select a plot to display:', plot_options_no_ext)
                
                # Display the selected plot
                st.image(os.path.join(plot_directory, selected_plot + os.path.splitext(plot_options[0])[1]), 
                        width=None)
            else:
                st.warning("No image files found in the plots directory.")
                st.info("Please add some .png, .jpg, or .jpeg files to the plots directory.")
    except Exception as e:
        st.error(f"Error accessing plots directory: {str(e)}")

# Segmentation and Clustering page
elif page == 'Segmentation & Clustering':
    st.title('Segmentation & Clustering')
    st.write('Discover patterns in your data through advanced clustering techniques.')
    
    # Replace radio button with tabs for method selection
    method_tab1, method_tab2 = st.tabs(["Demographic Preferences", "Purchase Behavior"])
    
    with method_tab1:
        # Elbow Method Analysis section for Demographics
        st.header("Optimal Number of Clusters Analysis")
        st.write("""
        Before applying our clustering approaches, we need to determine the optimal number of clusters.
        We use the Elbow Method, which plots the sum of squared distances against different numbers of clusters.
        The 'elbow' of this plot suggests the optimal number of clusters.
        """)
        
        try:
            st.image('interface/plots/clustering/demographic/elbow_method.png', width=None)
            st.write("""
            **Analysis of Elbow Method Results:**
            - The graph shows a clear elbow at k=4 clusters
            - After this point, the reduction in distortion becomes much smaller
            - This suggests that 4 clusters provide a good balance between cluster count and explanation of variance
            """)
        except Exception as e:
            st.error(f"Error loading elbow method plot: {str(e)}")

        # Demographic clustering analysis tabs
        demo_tab1, demo_tab2, demo_tab3, demo_tab4, demo_tab5 = st.tabs([
            "Hierarchical + K-means",
            "SOM + K-means",
            "SOM + Hierarchical",
            "DBSCAN",
            "Combined Results"
        ])
        
        with demo_tab1:
            st.subheader("Hierarchical + K-means Clustering")
            try:
                # Silhouette Analysis
                st.write("### Silhouette Analysis")
                st.image('interface/plots/clustering/demographic/hierarchical_kmeans/silhouette.png', 
                       width=None)
                st.write("""
                The silhouette analysis validates our cluster selection:
                - Higher silhouette scores indicate better-defined clusters
                - Shows how well-separated the resulting clusters are
                """)
                
                # Cluster Profiles
                st.write("### Cluster Profiles")
                st.image('interface/plots/clustering/demographic/hierarchical_kmeans/cluster_profiles_3.png', 
                       width=None)
                st.write("""
                Analysis of 3-cluster solution:
                - Shows the distribution of features across three distinct groups
                - Each cluster represents a different customer segment
                - We can observe the main characteristics that define each group
                """)
                
                st.image('interface/plots/clustering/demographic/hierarchical_kmeans/cluster_profiles_4.png', 
                       width=None)
                st.write("""
                Analysis of 4-cluster solution:
                - Provides a more granular segmentation
                - Shows how the segments split when adding another cluster
                - Allows comparison between 3 and 4 cluster solutions
                """)
            except Exception as e:
                st.error(f"Error loading Hierarchical + K-means visualizations: {str(e)}")
                
        with demo_tab2:
            st.subheader("SOM + K-means Clustering")
            try:
                # Hit Map View
                st.write("### SOM Hit Map")
                st.image('interface/plots/clustering/demographic/som_kmeans/hitMapView.png', 
                       width=None)
                st.write("""
                The SOM hit map shows the distribution of data points across the self-organizing map:
                - Each cell represents a node in the SOM
                - Colors indicate the density of data points mapped to each node
                """)
                
                # Inertia Plot
                st.write("### Inertia Analysis")
                st.image('interface/plots/clustering/demographic/som_kmeans/inertia.png', 
                       width=None)
                st.write("Shows the convergence of the SOM algorithm")

                # Final Clusters
                st.write("### Final Clusters")
                st.image('interface/plots/clustering/demographic/som_kmeans/final_cluster.png',
                       width=None)
                st.write("Visualization of the final cluster assignments")
            except Exception as e:
                st.error(f"Error loading SOM + K-means visualizations: {str(e)}")
                
        with demo_tab3:
            st.subheader("SOM + Hierarchical Clustering")
            try:
                # Hit Map View
                st.write("### SOM Hit Map")
                st.image('interface/plots/clustering/demographic/som_hierarchichal/hitMapView.png', 
                       width=None)
                
                # Dendrogram
                st.write("### Hierarchical Clustering Dendrogram")
                st.image('interface/plots/clustering/demographic/som_hierarchichal/dendogram.png', 
                       width=None)
                
                # Cluster Profiles
                st.write("### Cluster Profiles")
                st.image('interface/plots/clustering/demographic/som_hierarchichal/cluster_profiles_6.png', 
                       width=None)
            except Exception as e:
                st.error(f"Error loading SOM + Hierarchical visualizations: {str(e)}")
                
        with demo_tab4:
            st.subheader("DBSCAN Clustering")
            try:
                # Epsilon Selection
                st.write("### Epsilon Parameter Selection")
                st.image('interface/plots/clustering/demographic/dbscan/eps.png', 
                       width=None)
                st.image('interface/plots/clustering/demographic/dbscan/epsZoom.png', 
                       width=None)
                
                # Cluster Profiles
                st.write("### Cluster Profiles")
                st.image('interface/plots/clustering/demographic/dbscan/cluster_profiles_5.png', 
                       width=None)
            except Exception as e:
                st.error(f"Error loading DBSCAN visualizations: {str(e)}")
                
        with demo_tab5:
            st.subheader("Combined Results")
            try:
                st.write("### Cluster Profiling Comparison")
                st.image('interface/plots/clustering/demographic/combined_results/cluster_profiling.png', 
                       width=None)
                st.write("""
                Comparison of clustering results across different methods:
                - Shows how different approaches segment the customers
                - Helps identify consistent patterns across methods
                - Highlights the strengths of each approach
                """)
            except Exception as e:
                st.error(f"Error loading combined results: {str(e)}")
            
    with method_tab2:
        # Elbow Method Analysis section for Purchase Behavior
        st.header("Optimal Number of Clusters Analysis")
        st.write("""
        Before applying our clustering approaches, we need to determine the optimal number of clusters.
        We use the Elbow Method, which plots the sum of squared distances against different numbers of clusters.
        The 'elbow' of this plot suggests the optimal number of clusters.
        """)
        
        try:
            st.image('interface/plots/clustering/purchase/elbow_method.png', width=None)
            st.write("""
            **Analysis of Elbow Method Results:**
            - The elbow curve indicates an optimal point at k=3 clusters
            - The distortion score stabilizes after this point
            - This suggests that 3 distinct purchase behavior patterns exist in our data
            """)
            
            # Purchase behavior clustering analysis tabs
            purchase_tab1, purchase_tab2, purchase_tab3, purchase_tab4, purchase_tab5 = st.tabs([
                "Hierarchical + K-means",
                "SOM + K-means",
                "SOM + Hierarchical",
                "DBSCAN",
                "Combined Results"
            ])

            with purchase_tab1:
                st.subheader("Hierarchical + K-means Clustering")
                try:
                    st.write("### Silhouette Analysis")
                    st.image('interface/plots/clustering/purchase/hierarchical_kmeans/silhouette.png', 
                           width=None)
                    
                    st.write("### Final Cluster")
                    st.image('interface/plots/clustering/purchase/hierarchical_kmeans/final_cluster.png', 
                           width=None)
                except Exception as e:
                    st.error(f"Error loading Hierarchical + K-means visualizations: {str(e)}")
            
            with purchase_tab2:
                st.subheader("SOM + K-means Clustering")
                try:
                    st.write("### Inertia Analysis") 
                    st.image('interface/plots/clustering/purchase/som_kmeans/inertia.png',
                           width=None)
                    st.write("""
                    Beyond 3 clusters, the decrease in inertia slows down, which suggests diminishing returns for adding more clusters.
                    
                    The "elbow point" appears to be at 3 clusters, where the rate of improvement in inertia reduction becomes less pronounced.
                    """)
                    
                    st.write("### Hit Map View")
                    st.image('interface/plots/clustering/purchase/som_kmeans/hitMapView.png',
                           width=None)
                    
                    st.write("### Final Cluster")
                    st.image('interface/plots/clustering/purchase/som_kmeans/final_cluster_3.png',
                           width=None)
                except Exception as e:
                    st.error(f"Error loading SOM + K-means visualizations: {str(e)}")
            with purchase_tab3:
                st.subheader("SOM + Hierarchical Clustering")
                try:
                    st.write("### Dendrogram")
                    st.image('interface/plots/clustering/purchase/som_hierarchical/dendogram.png', 
                           width=None)
                    st.write("""
                    The threshold (red line) intersects just below a noticeable "gap" in the dendrogram.
                    Above this threshold, the vertical distances between clusters are much larger, meaning clusters are more distinct.

                    Based on this analysis 6 is the right choice.
                    """)
                    
                    st.write("### Hit Map View")
                    st.image('interface/plots/clustering/purchase/som_hierarchical/hitMapView.png', 
                           width=None)
                    
                    st.write("### Final Cluster")
                    st.image('interface/plots/clustering/purchase/som_hierarchical/final_cluster.png', 
                           width=None)
                except Exception as e:
                    st.error(f"Error loading SOM + Hierarchical visualizations: {str(e)}")
                    
            with purchase_tab4:
                st.subheader("DBSCAN Clustering")
                try:
                    st.write("### Epsilon Parameter Selection")
                    st.image('interface/plots/clustering/purchase/dbscan/eps.png', 
                           width=None)
                    st.write("### Zooming in on the elbow part")
                    st.image('interface/plots/clustering/purchase/dbscan/epsZoom.png', 
                           width=None)
                    
                    st.write("### Cluster Profiling")
                    st.image('interface/plots/clustering/purchase/dbscan/cluster_profiling.png', 
                           width=None)
                except Exception as e:
                    st.error(f"Error loading DBSCAN visualizations: {str(e)}")
                    
            with purchase_tab5:
                st.subheader("Combined Results")
                try:
                    st.write("### Combined Cluster Analysis")
                    st.image('interface/plots/clustering/purchase/combined_clusters/combined_clusters.png', 
                           width=None)
                except Exception as e:
                    st.error(f"Error loading combined results: {str(e)}")

        except Exception as e:
            st.error(f"Error loading purchase behavior analysis: {str(e)}")

# Final Clusterization page
else:
    st.title('Final Clusterization')
    st.write('View the final clustering results and customer segments.')
    
    # Create tabs for different clustering approaches
    final_tab1, final_tab2, final_tab3 = st.tabs([
        "Demographic Segments", 
        "Purchase Behavior Segments",
        "3D Cluster Visualization"
    ])
    
    with final_tab1:
        st.header("Final Demographic Segments")
        try:
            st.image('interface/plots/final/demographic_segments.png', width=None)
            st.write("""
            ### Key Demographic Segments:
            - Detailed breakdown of final customer segments
            - Key characteristics of each group
            - Segment size and distribution
            """)
        except Exception as e:
            st.error(f"Error loading demographic segments: {str(e)}")
    
    with final_tab2:
        st.header("Final Purchase Behavior Segments")
        try:
            st.image('interface/plots/final/purchase_segments.png', width=None)
            st.write("""
            ### Key Purchase Behavior Segments:
            - Purchase patterns for each segment
            - Spending habits and preferences
            - Transaction frequency analysis
            """)
        except Exception as e:
            st.error(f"Error loading purchase behavior segments: {str(e)}")
    
    with final_tab3:
        st.header("3D Cluster Visualization")
        try:
            # Load the data with cluster labels
            df = pickle.load(open("preprocessed_data_numerical.pkl", "rb"))
            
            # Create the 3D scatter plot using Plotly Express
            fig = px.scatter_3d(
                df,
                x='log_order_rate_per_week',
                y='log_amount_spent_per_week',
                z='chain_percentage',
                color='customer_age',  # Changed from 'merged_labels' to an available column
                labels={
                    'log_order_rate_per_week': 'Order Rate (log)',
                    'log_amount_spent_per_week': 'Amount Spent (log)',
                    'chain_percentage': 'Chain Percentage',
                    'customer_age': 'Customer Age'
                },
                title='Customer Distribution in 3D Space'
            )

            # Update the layout for better visualization
            fig.update_layout(
                scene=dict(
                    xaxis_title='Order Rate (log)',
                    yaxis_title='Amount Spent (log)',
                    zaxis_title='Chain Percentage'
                ),
                margin=dict(l=0, r=0, b=0, t=30)
            )

            # Display the plot in Streamlit
            st.plotly_chart(fig, use_container_width=True)
            
            st.write("""
            ### 3D Visualization of Customer Distribution
            
            This interactive 3D plot shows how customers are distributed based on three key metrics:
            - **Order Rate**: Frequency of purchases (log-transformed)
            - **Amount Spent**: Total spending per week (log-transformed)
            - **Chain Percentage**: Preference for chain establishments
            
            Points are colored by customer age to show additional patterns.
            
            You can:
            - Rotate the plot by clicking and dragging
            - Zoom in/out using the scroll wheel
            - Double click to reset the view
            - Hover over points to see detailed information
            """)

        except Exception as e:
            st.error(f"Error loading 3D visualization: {str(e)}")
            st.info("Please make sure the data file is available and contains the required columns.")
