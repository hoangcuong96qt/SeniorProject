import { Component, OnInit } from '@angular/core';
import { logoList } from "./logoList";
import { TranslateService } from "@ngx-translate/core";

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  logos = logoList;
  constructor(public translate: TranslateService) { 
    translate.use('vi');
  }

  ngOnInit() {
  }

}