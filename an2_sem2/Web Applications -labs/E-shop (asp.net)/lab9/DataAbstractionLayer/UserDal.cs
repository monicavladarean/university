using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using lab9.Models;
using MySql.Data.MySqlClient;

namespace lab9.DataAbstractionLayer
{
    public class UserDal
    {
        public User GetUser(string username, string password)
        {
            MySqlConnection connection;
            string connectionString = "server=localhost;uid=root;pwd=;database=store;";

            connection = new MySqlConnection();
            connection.ConnectionString = connectionString;
            connection.Open();

            MySqlCommand command = new MySqlCommand();
            command.Connection = connection;
            command.CommandText =
                "select * from users where username='" + username + "' and password='" + password + "'";
            MySqlDataReader dataReader = command.ExecuteReader();

            User user = null;

            if (dataReader.Read())
            {
                user = new User(dataReader.GetInt32("userID"), dataReader.GetString("username"), dataReader.GetString("password"));

            }
            dataReader.Close();
            return user;
        }
    }
}