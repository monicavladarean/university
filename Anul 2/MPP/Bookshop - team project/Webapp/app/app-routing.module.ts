import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ClientsComponent} from "./clients/clients.component";
import {BooksComponent} from "./books/books.component";


const routes: Routes = [
  {path:'clients',component:ClientsComponent},
  {path:'books',component:BooksComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
