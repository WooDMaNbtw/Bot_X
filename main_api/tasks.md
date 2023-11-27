# Tasks

## 1
Имеются api-методы:
- регистрация:
  POST http://yadro.ru/api/v0/apps/{appId}/users
  Request:
  {email: "string", password: "string"}
  Responses:
  {status: 200, user_id: "integer"}
  {status: 400, error: "Bad email"}

- авторизация:
  POST http://yadro.ru/api/v0/apps/{appId}/users/login
  Request:
  {email: "string", password: "string"}
  Responses:
  {status: 200, access_token: "string"}
  {status: 400, error: "Bad email"}
  {status: 401, error: "Bad email or password"}

Необходимо сделать отдельный фейковый сервис с этими методами, а именно заглушки:
 - Когда на регистрацию отправляем: {email: "admin@admin.ru", password: "qwerty123456"}, он должен вернуть ответ: {status: 200, user_id: 1}
 - Когда на регистрацию отправляем: {email: "admin", password: "qwerty123456"}, он должен вернуть ответ: {status: 400, error: "Bad email"}
 
 - Когда на авторизацию отправляем: {email: "admin@admin.ru", password: "qwerty123456"}, он должен вернуть ответ: {status: 200, access_token: "abcd"}
 - Когда на авторизацию отправляем: {email: "admin", password: "qwerty123456"}, он должен вернуть ответ: {status: 400, error: "Bad email"}
 - Когда на авторизацию отправляем: {email: "любой email", password: "любой password"}, он должен вернуть ответ: {status: 401, error: "Bad email or password"}

Примечание: {appId} - это динамический application id и он должен быть равен: 123-456-789-000





# 2

На основе паттерна https://refactoring.guru/ru/design-patterns/template-method (шаблонный метод) создать следующую структуру классов:

// Базовый интерфейс:
## interface RouteInterface {
  ### public function setParameters( array $data ):array;
  ### public function getParameters():array;
  ### public function setResponse( array $data ):array;
  ### public function getResponse():array;
  ### public function send( string $uri, string $method = 'GET' ):void;
}

// Базовый класс Route
## class Route implements RouteInterface {
  const APP_ID = '123-456-789-000';
  protected $parameters = [];
  protected $response = [];

  // Реализовываем метод из интерфейса
##  public function setParameters( array $data ):array {
    // логика оборачивания данных под данные сервиса yadro.ru, т.е. модифицируем тут $data

    $this->parameters = $data; // Сохраняем модифицированную $data в свойство $this->parameters
  }

  // Реализовываем метод из интерфейса
##  public function getParameters():array {
    return $this->parameters;
  }

  // Реализовываем метод из интерфейса
##  public function setResponse( array $data ):array {
    // логика оборачивания данных из данных сервиса yadro.ru под свои данные, т.е. модифицируем тут $data

    $this->response = $data; // Сохраняем модифицированную $data в свойство $this->response
  }

  // Реализовываем метод из интерфейса
##  public function getResponse():array {
    return $this->response;
  }

  // Реализовываем метод из интерфейса
##  public function send( string $uri, string $method = 'GET' ):void {
    $url = 'http://yadro.ru/api/v0/apps/' . self::APP_ID . $uri;
    // делаем запрос на $url с методом $method  и данными из свойства $this->parameters
    // полученные данные сохраняем, вызывая метод $this->setResponse( $response ); 
  }
}


// Создаём свой класс RegUserRoute:
## class RegUserRoute extends Route {
  // Переопределяем родительский метод из базового класса Route
  public function send():void {
    // Какая-то своя логика приложения дополнительная
    parent::send('/users', 'POST'); // Вызываем родительский метод
  }
}

// Создаём свой класс AuthUserRoute:
## class AuthUserRoute extends Route {
  // Переопределяем родительский метод из базового класса Route
  public function send():void {
    // Какая-то своя логика приложения дополнительная
    parent::send('/users/login', 'POST'); // Вызываем родительский метод
  }
}

// Дальше уже эти классы прокидываем в свои апи-методы
// Тут делаем аналогичный метод запроса как у yadro.ru, но только без appId, т.к. он из константы будет проставляться
Api::post('/api/v0/users', 'RegUserRoute::send');
Api::post('/api/v0/users/login', 'AuthUserRoute::send');