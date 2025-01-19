# Mini-Lesson 14.2: Using Graphivz

Decision trees are among the most popular supervised learning method algorithms because they are utilized to solve various business problems. In addition to being used for regression and classification, decision trees do not require features to be sized, and they can be visualized readily, making them relatively easy to interpret. Therefore, using this method will not only help you understand your model better but also help you prove its efficacy. Consequently, it is helpful to know how to create a visualization using your model, and Graphviz is a great tool to help you accomplish this.

## Overview

Graphviz is open-source graph visualization software that allows you to represent structural information as diagrams of abstract graphs and networks. Here are some key features of Graphviz:

- **Automatic layout**: Graphviz manages the layout of nodes and edges, ensuring an attractively pleasing and organized visualization.
- **Customization**: While the layout is automated, you can still customize different aspects of the graph, such as colors, fonts, and styles.
- **Compatibility**: It works smoothly across different browsers, allowing your visualizations to reach a wider audience.
- **Dynamic updates**: It supports dynamic updates, making it useful for interactive applications.

## Implementation

You can use Graphviz to visualize a decision tree created using scikit-learn. Here is how you can do that:

1. Make sure you have Graphviz installed. You can install it using:
```python
pip install graphviz
```

2. Create a decision tree model using scikit-learn:
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

model = DecisionTreeClassifier()
model.fit(X, y)  # Replace X and y with your data
```

3. Export the decision tree to the DOT format using tree.export_graphviz:
```python
dot_data = tree.export_graphviz(model,
                               feature_names=feature_names,
                               class_names=class_names,
                               filled=True,
                               rounded=True,
                               special_characters=True,
                               out_file=None)
```

4. Create a Graphviz source object and display it:
```python
from graphviz import Source
graph = Source(dot_data)
graph.view()
```

## Advantages and Limitations

### Pros
- Includes several packages and libraries, including ones for graphics, utilities, and drawing
- Has a graphical user interface that is interactive and web-based
- Built on the DOT language
- Offers some auxiliary tools

### Cons
- Has very disorganized learning documentation
- Lacks the community support offered by other open-source tools
- Lacks support for geospatial data
- Cannot support GUI editors
- Is impossible to integrate with other third-party tools

## Additional Resources
To learn more about Graphviz, please visit the [Graphviz website](https://graphviz.org/). Additionally, if you want to install Graphviz, these [installation instructions](https://graphviz.org/download/) may be useful.