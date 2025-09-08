from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

def get_product_category_pairs_and_uncategorized(
    products_df, categories_df, product_category_links_df
):
    """
    Возвращает датафрейм со всеми парами "Имя продукта - Имя категории"
    и продуктами без категорий.

    Args:
        products_df (DataFrame): Датафрейм с продуктами.
        categories_df (DataFrame): Датафрейм с категориями.
        product_category_links_df (DataFrame): Датафрейм со связями.

    Returns:
        DataFrame: Датафрейм с колонками 'product_name' и 'category_name'.
    """
    # Выполняем left outer join, чтобы сохранить все продукты,
    # даже если у них нет категорий.
    joined_df = products_df.join(
        product_category_links_df, "product_id", "left_outer"
    ).join(categories_df, "category_id", "left_outer")

    # Выбираем только нужные колонки и сортируем для удобства.
    result_df = joined_df.select(
        col("product_name"), col("category_name")
    ).orderBy("product_name", "category_name")

    return result_df