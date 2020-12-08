using lab9.DataAbstractionLayer;
using lab9.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace lab9.Controllers
{
    public class LoginController : Controller
    {
        [HttpPost]
        public ActionResult Login(User user)
        {
            if (ModelState.IsValid)
            {
                var userDal = new UserDal();
                var obj = userDal.GetUser(user.Username, user.Password);
                if (obj != null)
                {
                    Session["UserID"] = obj.Id.ToString();
                    Session["Username"] = obj.Username;
                    return RedirectToAction("HomePage", "Main");
                }
            }

            return View("Login");
        }

        [HttpGet]
        public ActionResult Login()
        {
            return View();
        }
    }
}