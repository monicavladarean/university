using lab9.Models;
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace lab9.DataAbstractionLayer
{
    public class BasketItemDal
    {
        private string _connectionString = "server=localhost;uid=root;pwd=;database=store;";
        public List<BasketItem> GetAllBasketForUser(string username)
        {
            MySqlConnection connection;
            List<BasketItem> basket = new List<BasketItem>();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                string sql = "";
                sql = "select * from shoppingbasket where username=@username";

                MySqlCommand command = new MySqlCommand();
                command.CommandText = sql;
                command.Parameters.AddWithValue("@username", username);
                command.Connection = connection;
                MySqlDataReader dataReader = command.ExecuteReader();

                while (dataReader.Read())
                {
                    int id = dataReader.GetInt32("id");
                    int productId = dataReader.GetInt32("productId");
                    int quantity = dataReader.GetInt32("quantity");
                    string usernameDB = dataReader.GetString("username");

                    BasketItem basketItem = new BasketItem(id, productId,quantity,usernameDB);
                    basket.Add(basketItem);
                }
                dataReader.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }

            return basket;
        }

        public BasketItem GetBasketItemById(int id)
        {
            MySqlConnection connection;
            BasketItem basketItem = new BasketItem();

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                string sql = "select * from shoppingbasket where id=@id";

                MySqlCommand command = new MySqlCommand();
                command.CommandText = sql;
                command.Parameters.AddWithValue("@id", id);
                command.Connection = connection;
                MySqlDataReader dataReader = command.ExecuteReader();

                if (dataReader.Read())
                {
                    int idBD = dataReader.GetInt32("id");
                    int productId = dataReader.GetInt32("productId");
                    int quantity = dataReader.GetInt32("quantity");
                    string username = dataReader.GetString("username");

                    basketItem = new BasketItem(idBD, productId,quantity,username);
                }
                dataReader.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                throw;
            }

            return basketItem;
        }

        public void DeleteBasketItem(int id)
        {
            MySqlConnection connection;

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                MySqlCommand command = new MySqlCommand();
                string sql = "delete from shoppingbasket where id=@id";
                command.CommandText = sql;
                command.Parameters.AddWithValue("@id", id);
                command.Connection = connection;
                command.ExecuteNonQuery();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        public void SaveBasketItem(BasketItem basketItem)
        {
            MySqlConnection connection;

            try
            {
                connection = new MySqlConnection();
                connection.ConnectionString = _connectionString;
                connection.Open();

                MySqlCommand command = new MySqlCommand();
                string sql = "insert into shoppingbasket (productId,quantity,username) values (@productId,@quantity,@username)";
                command.CommandText = sql;
                command.Parameters.AddWithValue("@productId", basketItem.ProductId);
                command.Parameters.AddWithValue("@quantity", basketItem.Quantity);
                command.Parameters.AddWithValue("@username", basketItem.Username);
                command.Connection = connection;
                command.ExecuteNonQuery();
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

    }
}