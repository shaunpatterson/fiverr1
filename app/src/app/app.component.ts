import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';

export class Test {
    id?: number;
    test?: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'app';

  public test?: Test;

  constructor(private http: HttpClient) {}

  public ngOnInit(): void {
      this.http.get<Test>('/api/test').subscribe((t) => {
          this.test = t;
      });
  }

}
