# Helper functions and classes used in modeling

import pandas

from sklearn.base            import BaseEstimator, TransformerMixin
from sklearn.pipeline        import Pipeline
from sklearn.preprocessing   import FunctionTransformer
from sklearn.model_selection import cross_val_score


def score(models, preprocessor, X, y):
    """
    Score the given model and preprocessor combinations on the given dataset
    """

    scores = []
    index  = []
    
    for model_name, model in models:
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('model'       , model)
        ])

        mae = -cross_val_score(
            pipeline, X, y,
            n_jobs=-1, scoring="neg_mean_absolute_error", error_score="raise"
        ).mean()
        rmse = -cross_val_score(
            pipeline, X, y,
            n_jobs=-1, scoring="neg_root_mean_squared_error", error_score="raise"
        ).mean()
        r2 = cross_val_score(
            pipeline, X, y,
            n_jobs=-1, scoring="r2", error_score="raise"
        ).mean()
        
        scores.append(
            (
                int(mae.round(-3)),
                int(rmse.round(-3)),
                r2.round(2)
            )
        )
        index.append(model_name)

    return pandas.DataFrame(
        scores,
        index=index,
        columns=["MAE", "RMSE", "r²"]
    )

def restore_columns(X, columns):
    """
    Wraps data into a DataFrame with given column names
    """
    return pandas.DataFrame(X, columns=columns)


class ColumnMapper(BaseEstimator, TransformerMixin):
    """
    Maps given column to new values using given mapping
    and adds the results as a new column
    """

    def __init__(self, column, mapping):
        self.column  = column
        self.mapping = mapping

    def fit(self, X, y=None):
        return self

    def transform(self, X):      
        X_transformed = X.copy()
        X_transformed[f"{self.column}_mapped"] = X[self.column].map(self.mapping)
        
        return X_transformed

class RowApplier(BaseEstimator, TransformerMixin):
    """
    Applies given function to each row and adds the results as a new column
    """

    def __init__(self, function):
        self.function = function

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_transformed = X.copy()
        X_transformed[f"{self.function.__name__}"] = X.apply(self.function, axis=1)

        return X_transformed

class ColumnRestorer(FunctionTransformer):
    """
    Used in pipeline to restore column names between preprocessing steps
    """
    
    def __init__(self, columns):
        self.columns = columns
        super().__init__(
            func=restore_columns,
            validate=False,
            kw_args={"columns": self.columns}
        )
