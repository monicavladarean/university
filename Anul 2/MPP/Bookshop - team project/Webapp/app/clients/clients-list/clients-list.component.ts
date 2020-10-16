import { Component, OnInit } from '@angular/core';
import {Client} from "../shared/client.model";
import {Router} from "@angular/router";
import {ClientService} from "../shared/client.service";

@Component({
  selector: 'app-clients-list',
  templateUrl: './clients-list.component.html',
  styleUrls: ['./clients-list.component.css']
})
export class ClientsListComponent implements OnInit {
  clients:Array<Client>;
  errorMessage:string;
  constructor(private router:Router,private clientService:ClientService) { }

  ngOnInit(): void {
    this.getClients();
  }

  getClients()
  {
    this.clientService.getClients().subscribe(clients => this.clients = clients,
                                              error => this.errorMessage = <any> error);
  }

}
