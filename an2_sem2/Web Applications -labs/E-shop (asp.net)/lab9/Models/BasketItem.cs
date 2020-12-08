using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;

namespace lab9.Models
{
    public class BasketItem
    {
        public BasketItem(int id,int productId, int quantity, string username)
        {
            Id = id;
            ProductId = productId;
            Quantity = quantity;
            Username = username;
        }

        public BasketItem()
        {
        }

        public int Id { get; set; }

        [RegularExpression(@"^[0-9]+[0-9'\s]*$")]
        [Required]
        public int ProductId { get; set; }

        [RegularExpression(@"^[0-9]+[0-9'\s]*$")]
        [Required]
        public int Quantity { get; set; }

        public string Username { get; set; }
    }
}