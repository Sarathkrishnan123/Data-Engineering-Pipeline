import psycopg2
from sqlalchemy import create_engine

def load_data_frame_to_postgresql(df, table_name, connection_string):
    """
    Load a pandas DataFrame into a PostgreSQL table.

    Parameters:
        df (pandas.DataFrame): The DataFrame to be loaded into the database.
        table_name (str): The name of the PostgreSQL table.
        connection_string (str): The connection string for the PostgreSQL database.

    Returns:
        None
    """
    try:
        # Create a connection to the PostgreSQL database
        engine = create_engine(connection_string)
        conn = engine.raw_connection()
        cursor = conn.cursor()

        # Convert DataFrame to SQL table and insert into the database
        df.to_sql(table_name, con=engine, if_exists='replace', index=False, method='multi')
        status="success"

        # Commit the transaction
        conn.commit()
        print(f"DataFrame successfully loaded into the '{table_name}' table.")
        text=f"DataFrame successfully loaded into the '{table_name}' table."
        return status,text

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        status="fail"
        text=f"Error: {error}"
        return status,text


# Example usage:
# Replace the values with your actual DataFrame, table name, and connection string
# load_data_frame_to_postgresql(df, 'your_table_name', 'postgresql://username:password@localhost:5432/your_database')
