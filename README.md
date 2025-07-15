# disk-access-pointcloud
Binary tree indexing &amp; querying of point clouds with limited memory (Big Data project)
Disk Access Model – Point Cloud Binary Tree
Big Data Algorithms Project — April 2025
Author: Lora Velevska
University: South-West University “Neofit Rilski”
Erasmus+ Exchange: University of Maribor, Slovenia

Project Overview
This project addresses the challenge of working with point cloud data (X, Y, Z coordinates) that is too large to fit in memory (RAM).

The goal is to preprocess this data by:

Sorting it using a disk-based algorithm

Building a binary tree by recursively dividing the space

Allowing fast bounding box (BBOX) queries using the tree structure

The tree and data are stored in files, enabling fast search without exceeding memory limits.

Input Example
X         Y         Z
394372.82 39305.84  235.3  
394374.82 39305.82  233.7  
394373.82 39305.83  231.2  
394375.82 39305.81  236.0  
...
🛠 Technologies Used
Python (or other)

File-based data processing

External Merge Sort

Recursive binary tree structure

Bounding box search algorithm

Optional: matplotlib (for visualization)

Functionality
Part 0 – External Sorting Algorithm
Sorts data using disk-based external merge sort

Handles memory limitation of 10MB

Writes sorted chunks to disk and merges recursively

Part 1 – Constructing the Binary Tree
Recursively divides point cloud by alternating X and Y

Saves median splits and file references in a tree

Each node contains the median value; leaves contain file paths

Stops when each file has ≤10MB worth of points

Part 2 – Fast Queries on the Tree
Input: xmin, xmax, ymin, ymax

Tree is traversed recursively based on BBOX

When a leaf is reached, its file is loaded and filtered

Only matching points are returned

Optional: result is plotted using visualization

Query Example
# Bounding box input
bbox = {
    "xmin": 394370,
    "xmax": 394374,
    "ymin": 39305.80,
    "ymax": 39305.85
}
Bonus Visualization (Optional)
Students who visualize:

The binary tree structure

The resulting point cloud from a BBOX query
