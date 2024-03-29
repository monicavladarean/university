import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Book} from "./book.model";

@Injectable({
  providedIn: 'root'
})
export class BookService {
  private booksUrl = 'http://localhost:8080/api/books';
  constructor(private httpClient: HttpClient) { }
  getBooks():Observable<Book[]>
  {
    return this.httpClient.get<Array<Book>>(this.booksUrl);
  }
}
