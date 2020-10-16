import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {Book} from "../shared/book.model";
import {BookService} from "../shared/book.service";

@Component({
  selector: 'app-books-list',
  templateUrl: './books-list.component.html',
  styleUrls: ['./books-list.component.css']
})
export class BooksListComponent implements OnInit {
  books:Array<Book>;
  errorMessage:string;
  constructor(private router:Router,private bookService:BookService) { }

  ngOnInit(): void {
    this.getBooks();
  }

  getBooks()
  {
    this.bookService.getBooks().subscribe(books => this.books = books,
                                          error => this.errorMessage = <any> error);
  }
}
