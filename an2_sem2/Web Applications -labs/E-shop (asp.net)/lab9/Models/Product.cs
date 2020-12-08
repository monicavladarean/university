using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;

namespace lab9.Models
{
    public class Product
    {
        public Product(int id, string name, int price, string description)
        {
            Id = id;
            Name = name;
            Price = price;
            Description = description;
        }

        public Product()
        {
        }

        public int Id { get; set; }

        [RegularExpression(@"^[A-Z]+[a-zA-Z'\s]*$")]
        [Required]
        [StringLength(50)]
        public string Name { get; set; }

        [RegularExpression(@"^[0-9]+[0-9'\s]*$")]
        [Required]
        public int Price { get; set; }

        [RegularExpression(@"^[A-Z]+[a-zA-Z'\s]*$")]
        [Required]
        [StringLength(50)]
        public string Description { get; set; }
    }
}