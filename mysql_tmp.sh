create table brain_choice (
  id int unsigned auto_increment,
  trade_id int not null,
  predict int not null,
  result int not null,
  primary key(id)
);

CREATE USER 'ruixin'@'localhost' IDENTIFIED BY '123';

grant all on caesar to 'ruixin'@'localhost';
