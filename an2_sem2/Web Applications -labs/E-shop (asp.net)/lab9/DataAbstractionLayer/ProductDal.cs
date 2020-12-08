using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using lab9.Models;
using MySql.Data.MySqlClient;

namespace lab9.DataAbstractionLayer
{
    public class ProductDal
    {
        private string _connectionString = "server=localhost;uid=root;pwd=;database=store;";
        public List<Product> GetAllProducts()
        {
            MySqlConnection connection;
            List<Product> products = new List<Product>();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                MySqlCommand command = new MySqlCommand();
                command.Connection = connection;
                command.CommandText = "select * from products";
                MySqlDataReader dataReader = command.ExecuteReader();

                while (dataReader.Read())
                {
                    int id = dataReader.GetInt32("id");
                    string name = dataReader.GetString("name");
                    int price = dataReader.GetInt32("price");
                    string description = dataReader.GetString("description");

                    Product product = new Product(id, name, price, description);
                    products.Add(product);
                }
                dataReader.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return products;
        }

        public List<Product> GetAllProductsByDescription(string description, int pageNo)
        {
            MySqlConnection connection;
            List<Product> products = new List<Product>();
            int offset = 4 * (pageNo - 1);

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                string sql = "";
                if (description.Equals(""))
                {
                    sql = "select * from products limit @offset , 4";
                }
                else
                {
                    sql = "select * from products where description=@description limit @offset , 4";
                }

                MySqlCommand command = new MySqlCommand();
                command.CommandText = sql;
                command.Parameters.AddWithValue("@description", description);
                command.Parameters.AddWithValue("@offset", offset);
                command.Connection = connection;
                MySqlDataReader dataReader = command.ExecuteReader();

                while (dataReader.Read())
                {
                    int id = dataReader.GetInt32("id");
                    string name = dataReader.GetString("name");
                    int price = dataReader.GetInt32("price");
                    string descriptionDB = dataReader.GetString("description");

                    Product product = new Product(id, name, price, descriptionDB);
                    products.Add(product);
                }
                dataReader.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }

            return products;
        }

        public Product GetProductById(int id)
        {
            MySqlConnection connection;
            Product product = new Product();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                string sql = "select * from products where id=@id";

                MySqlCommand command = new MySqlCommand();
                command.CommandText = sql;
                command.Parameters.AddWithValue("@id", id);
                command.Connection = connection;
                MySqlDataReader dataReader = command.ExecuteReader();

                if (dataReader.Read())
                {
                    int idBD = dataReader.GetInt32("id");
                    string name = dataReader.GetString("name");
                    int price = dataReader.GetInt32("price");
                    string description = dataReader.GetString("description");

                    product = new Product(idBD, name, price, description);
                }
                dataReader.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }

            return product;
        }
    }
}