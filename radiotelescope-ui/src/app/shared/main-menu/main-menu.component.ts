import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';
import { PrimeIcons } from 'primeng/api';
@Component({
  selector: 'app-main-menu',
  templateUrl: './main-menu.component.html',
  styleUrls: ['./main-menu.component.css'],
})
export class MainMenuComponent implements OnInit {
  items!: MenuItem[];
  constructor() {}

  ngOnInit(): void {
    this.items = [
      { label: 'Inicio', icon: PrimeIcons.GLOBE, routerLink: [''] },
      {
        label: 'Capturar datos',
        icon: PrimeIcons.DATABASE,
        items: [
          {
            label: 'Frecuencia única',
            icon: PrimeIcons.CHECK,
            routerLink: ['capture-data/single-frequency'],
          },
          {
            label: 'Barrido de frecuencias',
            icon: PrimeIcons.SORT_AMOUNT_UP,
            routerLink: ['capture-data/sweep-frequency'],
          },
        ],
      },
      {
        label: 'Analizar datos',
        icon: PrimeIcons.CHART_LINE,
        items: [
          {
            label: 'Espectro bandas sensadas',
            icon: PrimeIcons.WIFI,
            routerLink: ['analyze-data/spectrum'],
          },
          {
            label: 'Datos RAW',
            icon: PrimeIcons.CLOCK,
            routerLink: ['analyze-data/data-raw'],
          },
        ],
      },
    ];
  }
}
