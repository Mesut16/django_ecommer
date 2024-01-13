# Django E-Ticaret Sitesi

Bu proje, Django web çerçevesi kullanılarak geliştirilmiş basit bir e-ticaret sitesidir. Bu proje üzerinde ürün eklemek, satın almak, kullanıcı hesapları oluşturmak gibi temel e-ticaret işlevselliğini içermektedir.

## Kurulum

Projeyi yerel makinenize klonlamak ve çalıştırmak için aşağıdaki adımları takip edin:

1. Bu depoyu klonlayın:

    ```bash
    git clone https://github.com/Mesut16/eTicaret_Django.git
    ```

2. Proje dizinine gidin:

    ```bash
    cd eTicaret_Django
    ```

3. Virtual environment (sanal ortam) oluşturun:

    ```bash
    python -m venv venv
    ```

4. Virtual environment'ı etkinleştirin:

    - Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - Linux veya macOS:

        ```bash
        source venv/bin/activate
        ```

5. Gerekli bağımlılıkları yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

6. Veritabanını migre edin:

    ```bash
    python manage.py migrate
    ```

7. Projeyi çalıştırın:

    ```bash
    python manage.py runserver
    ```

8. Tarayıcıda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) adresine gidin.

## Kullanım

Proje başlatıldıktan sonra, tarayıcınızda [http://127.0.0.1:8000/](http://127.0.0.1:8000/) adresine giderek e-ticaret sitesini görebilir ve kullanabilirsiniz.


Teşekkür ederiz!
