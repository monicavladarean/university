using lab9.DataAbstractionLayer;
using lab9.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace lab9.Controllers
{
    public class MainController : Controller
    {
        // GET: Main
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult HomePage()
        {
            if (Session["UserID"] != null)
                return View();
            return RedirectToAction("Login", "Login");
        }

        public string GetProducts()
        {
            ProductDal productDal = new ProductDal();
            List<Product> products = productDal.GetAllProducts();
            ViewData["products"] = products;

            string result = "<thead><th>ID</th><th>Name</th><th>Price</th><th>Description</th></thead>";

            foreach (Product product in products)
            {
                result += "<tr class=\"rows\">" +
                          "<td>" + product.Id + "</td>" +
                          "<td>" + product.Name + "</td>" +
                          "<td>" + product.Price + "</td>" +
                          "<td>" + product.Description + "</td>" +
                          "</tr>";
            }

            return result;
        }

        public string GetProductsFilteredByDescription()
        {
            string description = Request.Params["description"];
            int offset = Int32.Parse(Request.Params["pageNo"]);
            ProductDal productDal = new ProductDal();

            List<Product> products = productDal.GetAllProductsByDescription(description,offset);
            ViewData["products"] = products;

            string result = "<thead><th>ID</th><th>Name</th><th>Price</th><th>Description</th></thead>";

            foreach (Product product in products)
            {
                result += "<tr class=\"rows\">" +
                          "<td>" + product.Id + "</td>" +
                          "<td>" + product.Name + "</td>" +
                          "<td>" + product.Price + "</td>" +
                          "<td>" + product.Description + "</td>" +
                          "</tr>";
            }

            return result;
        }

        public string GetBasketForUser()
        {
            string username = Session["Username"].ToString();

            BasketItemDal basketItemDal = new BasketItemDal();
            List<BasketItem> basket = basketItemDal.GetAllBasketForUser(username);
            ViewData["basket"] = basket;

            string result = "<thead><th>ID</th><th>ProductID</th><th>Quantity</th></thead>";

            foreach (BasketItem basketItem in basket)
            {
                result += "<tr class=\"rows\">" +
                          "<td>" + basketItem.Id + "</td>" +
                          "<td>" + basketItem.ProductId + "</td>" +
                          "<td>" + basketItem.Quantity + "</td>" +
                          "</tr>";
            }

            return result;
        }

        [HttpGet]
        public ActionResult ShowBasket()
        {
            return View("ShowMyBasket");
        }

        public JsonResult GetBasketItemById(int id)
        {
            BasketItemDal basketItemDal = new BasketItemDal();
            BasketItem basketItem = basketItemDal.GetBasketItemById(id);

            var Data = new
            {
                ok = true,
                id = id
            };
            return Json(basketItem, JsonRequestBehavior.AllowGet);
        }

        public ActionResult TakeBasketItem(string id, string productId, string quantity)
        {
            BasketItem basketItem = new BasketItem();
            basketItem.Id = Int32.Parse(id);
            basketItem.ProductId = Int32.Parse(productId);
            basketItem.Quantity = Int32.Parse(quantity);
            basketItem.Username = Session["Username"].ToString();
            return View("DeleteBasketItem", basketItem);
        }


        public ActionResult RemoveBasketItem()
        {
            BasketItemDal basketItemDal = new BasketItemDal();
            basketItemDal.DeleteBasketItem(Int32.Parse(Request.Params["id"]));
            return RedirectToAction("ShowBasket", "Main");
        }

        [HttpGet]
        public ActionResult AddToBasket()
        {
            return View("AddNewBasketItem");
        }

        [HttpPost]
        public ActionResult SaveBasketItem(BasketItem basketItem)
        {
            if (ModelState.IsValid)
            {
                BasketItemDal basketItemDal = new BasketItemDal();
                basketItem.Username = Session["Username"].ToString();
                basketItemDal.SaveBasketItem(basketItem);
                return RedirectToAction("ShowBasket", "Main");
            }

            return View("AddNewBasketItem");
        }
    }
}