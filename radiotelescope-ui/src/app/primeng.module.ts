import { NgModule } from '@angular/core';
import { MenubarModule } from 'primeng/menubar';
import { InputNumberModule } from 'primeng/inputnumber';
import { KnobModule } from 'primeng/knob';
import { SliderModule } from 'primeng/slider';
import { DropdownModule } from 'primeng/dropdown';

@NgModule({
  exports: [
    MenubarModule,
    InputNumberModule,
    KnobModule,
    SliderModule,
    DropdownModule,
  ],
})
export class PrimengModule {}
