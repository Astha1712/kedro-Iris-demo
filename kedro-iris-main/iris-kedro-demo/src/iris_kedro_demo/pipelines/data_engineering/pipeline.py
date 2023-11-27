"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import preprocessing, split_data , train_model, evaluate_model
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=preprocessing,
             inputs="iris",
             outputs=["X","y"]),

        node(func=split_data,
             inputs=["X","y","params:split"],
             outputs=["X_train", "X_test", "y_train", "y_test"]),

        node(func=train_model,
             inputs=["X_train", "y_train"],
             outputs="model"),

         node(func=evaluate_model,
             inputs=["model", "X_test", "y_test"],
             outputs=["accuracy", "report"]),
    ])
