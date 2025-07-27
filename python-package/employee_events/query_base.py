# Import any dependencies needed to execute sql queries
import pandas as pd
from typing import List
from .sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name: str = ""

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(cls) -> List[tuple]:
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    @classmethod
    def event_counts(cls, _id: int) -> pd.DataFrame:

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql = f"""
            SELECT   event_date,
                     SUM(positive_events)  AS positive_events,
                     SUM(negative_events)  AS negative_events
            FROM     employee_events
            JOIN     {cls.name}
                     USING({cls.name}_id)
            WHERE    {cls.name}.{cls.name}_id = {_id}
            GROUP BY event_date
            ORDER BY event_date
        """
        return cls.pandas_query(sql)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    @classmethod
    def notes(cls, _id: int) -> pd.DataFrame:

        sql = f"""
            SELECT   note_date,
                     note
            FROM     notes
            JOIN     {cls.name}
                     USING({cls.name}_id)
            WHERE    {cls.name}.{cls.name}_id = {_id}
            ORDER BY note_date
        """
        return cls.pandas_query(sql)

