import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from "@angular/common/http";

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {ClientsComponent} from './clients/clients.component';
import {ClientsListComponent} from './clients/clients-list/clients-list.component';
import {ClientService} from './clients/shared/client.service';
import { BooksComponent } from './books/books.component';
import { BooksListComponent } from './books/books-list/books-list.component';
import {BookService} from "./books/shared/book.service";

@NgModule({
  declarations: [
    AppComponent,
    ClientsComponent,
    ClientsListComponent,
    BooksComponent,
    BooksListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [ClientService,BookService],
  bootstrap: [AppComponent]
})
export class AppModule { }
