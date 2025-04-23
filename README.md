<h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Приложение для обмена сообщениями между людьми, созданное с помощью django-channels.
</font></font></h3>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Установка</font></font></h2><a id="user-content-installation" class="anchor" aria-label="Постоянная ссылка: Установка" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></div>
<ul>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 1</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Клонируйте исходный код с GitHub</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>git clone https://github.com/Viktoriya472/Chat.git
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="git clone https://github.com/Viktoriya472/GameApp.git
        " tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 2</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Создайте и используйте виртуальную среду (python 3.11) с помощью </font></font><code>venv</code>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python -m venv .venv
.venv/scripts/activate</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python -m venv .venv
.venv/scripts/activate" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 3</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Установите зависимости проекта</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>cd .\Chat\
pip install -r req.txt</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="cd .\GameApp\
pip install -r requirements.txt" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 4</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите миграции в базе данных</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python manage.py migrate
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="cd .\GameApp\
pip install -r requirements.txt" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 5</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите Redis для резервного хранения (в новом терминале)</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>docker run -p 6379:6379 -d redis:7
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="jmilkfansblog-manager server" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 6</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите сервер</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python manage.py runserver
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="jmilkfansblog-manager server" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"></font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Если возникает ошибка «ImportError: cannot import name 'DEFAULT_CHANNEL_LAYER'»</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python -m pip install -U channels["daphne"]
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="jmilkfansblog-manager server" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 7</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : </font></font>
  </li>
  <pre class="">Зарегистрируйтесь, авторизуйтесь, добавляйте контакты, создавайте чаты и отправляйте сообщения
 </pre>
</ul>
