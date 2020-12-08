using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;


namespace lab9.Models
{
    public class User
    {
        public User(int id, string username, string password)
        {
            Id = id;
            Username = username;
            Password = password;
        }

        public User()
        {
        }

        public int Id { get; set; }

        [Required]
        [MinLength(3)]
        [MaxLength(10)]
        public string Username { get; set; }

        [Required]
        public string Password { get; set; }
    }
}