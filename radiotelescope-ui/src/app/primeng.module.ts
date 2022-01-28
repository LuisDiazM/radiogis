import { NgModule } from '@angular/core';
import { MenubarModule } from 'primeng/menubar';
import { InputNumberModule } from 'primeng/inputnumber';
import { KnobModule } from 'primeng/knob';
import { SliderModule } from 'primeng/slider';
import { DropdownModule } from 'primeng/dropdown';
import { CardModule } from 'primeng/card';
import { ButtonModule } from 'primeng/button';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import {AvatarModule} from 'primeng/avatar';

@NgModule({
  exports: [
    MenubarModule,
    InputNumberModule,
    KnobModule,
    SliderModule,
    DropdownModule,
    CardModule,
    ButtonModule,
    ConfirmDialogModule,
    AvatarModule
  ],
})
export class PrimengModule {}
