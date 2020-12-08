import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { InventoryItem } from '../../app-logic/inventory-item';
import { InventoryListService } from '../../app-logic/inventory-list.service';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-add-item',
  templateUrl: './add-item.component.html',
  styleUrls: ['./add-item.component.css'],
})
export class AddItemComponent implements OnInit {
  addItemForm: FormGroup;
  item: InventoryItem;
  itemId: string;
  constructor(
    private fb: FormBuilder,
    private inventoryListService: InventoryListService,
    private route: Router,
    private activatedRoute: ActivatedRoute
  ) {
    this.activatedRoute.params.subscribe((params) => {
      this.itemId = params['id'];
    });
  }

  ngOnInit(): void {
    if (!this.itemId) {
      this.item = new InventoryItem();
      this.prepareForm();
    } else {
      this.inventoryListService.getDataById(this.itemId).subscribe((data) => {
        this.item = new InventoryItem(data);
        this.prepareForm();
      });
    }
  }

  prepareForm() {
    this.addItemForm = this.fb.group({
      name: [this.item.name, Validators.required],
      description: [this.item.description, Validators.maxLength(100)],
      user: [this.item.user, Validators.required],
      location: [this.item.location, Validators.required],
      inventoryNumber: [this.item.inventoryNumber, Validators.required],
      createdAt: [
        this.item.createdAt.toISOString().split('T')[0],
        Validators.required,
      ],
    });
  }

  onSubmit() {
    if (!this.itemId) {
      this.item = new InventoryItem(this.addItemForm.value);
      this.item.modifiedAt = new Date();
      this.item.active = false;

      this.inventoryListService.addData(this.item).subscribe(() => {
        this.route.navigate(['/inventory']);
      });
    } else {
      this.item.name = this.addItemForm.value.name;
      this.item.description = this.addItemForm.value.description;
      this.item.user = this.addItemForm.value.user;
      this.item.location = this.addItemForm.value.location;
      this.item.inventoryNumber = this.addItemForm.value.inventoryNumber;
      this.item.createdAt = new Date(this.addItemForm.value.createdAt);
      this.item.modifiedAt = new Date();

      this.inventoryListService.updateData(this.item).subscribe(() => {
        this.route.navigate(['/inventory']);
      });
    }
  }
  public hasError = (contrloName: string, errorName: string) => {
    return this.addItemForm.controls[contrloName].hasError(errorName);
  };
}
