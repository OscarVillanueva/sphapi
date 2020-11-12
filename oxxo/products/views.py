from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Beer
from .models import Order
from .models import Customer
from .serializers import BeerSerializer
from .serializers import CustomerSerializer
from .serializers import OrderSerializer

# Create your views here.
class BeerViewSet( viewsets.ModelViewSet ):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()

class BeerView( APIView ):
    # Validar que primero se haya solicitado un token
    permission_classes = (IsAuthenticated, )

    def get( self, request ):

        # Verificamos si viene un ID
        try:
            # Sacamos el id de la solicitud
            id = request.data["id"]

            # Buscamos la cerveza
            items = Beer.objects.get(id=id)

            print(items)

            # Pasamos a JSON
            serializer = BeerSerializer(items)

        except KeyError:
            # Sacamos todos las cervezas
            items = Beer.objects.all()

            # Pasamos JSON
            serializer = BeerSerializer(items, many=True)

        except Beer.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

        return Response({ "data": serializer.data }, status = status.HTTP_200_OK)

    # Insertar una cerveza
    def post( self, request ):
        # Construimos el objeto apartir de lo que llega por parametro
        serializer = BeerSerializer( data = request.data )

        # Verificamos si se pudo construir
        if serializer.is_valid():

            # Guardamos el objeto
            serializer.save()

            # Retornamos el objeto creado
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # Devolvemos los errores
            return Response({"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Actualizar una cerveza
    def put( self, request ):

        try:
            # Buscamos el objeto a actualizar
            item = Beer.objects.get(id=request.data['id'])
        except KeyError:

            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar un id"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Beer.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

        # Construimos el objeto
        serializer = BeerSerializer( instance = item, data = request.data, partial = True )

        # Verificamos si se logro construir
        if serializer.is_valid():

            # Actualizamos la BD
            serializer.save()

            # Retornamos el objeto actualizado
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        else:
            # Devolvemos los errores
            return Response({"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Borramos una cerveza
    def delete( self, request ):

        try:
            # Buscamos el objeto a actualizar
            item = Beer.objects.get(id=request.data['id'])
            item.delete()

            # Retornamos el objeto eliminado
            return Response({"data": "Eliminado correctamente"}, status=status.HTTP_202_ACCEPTED)

        except KeyError:

            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar un id"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Beer.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    # Endpoint para agregar un usuario
    def post( self, request ):
        try:

            # Sacamos los datos para crear al usuario
            username = request.data["username"]
            password = request.data["password"]

            # Creamos y guardamos
            user = User.objects.create_user(username, "", password)

            user.save()

            return Response({ "data": "Usuario creado correctamente" }, status=status.HTTP_201_CREATED)

        except KeyError:
            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar usuario y contraseña"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except IntegrityError:
            # Devolvemos los errores
            return Response({"errors": "Ese usuario ya existe"}, status=status.HTTP_406_NOT_ACCEPTABLE)

class CustomerView ( APIView ):
    # Validar que primero se haya solicitado un token
    permission_classes = (IsAuthenticated, )

    def get( self, request ):

        # Verificamos si viene un ID
        try:
            # Sacamos el id de la solicitud
            id = request.data["id"]

            # Buscamos la cerveza
            items = Customer.objects.get(id=id)

            # Pasamos a JSON
            serializer = CustomerSerializer(items)

        except KeyError:
            # Sacamos todos las cervezas
            items = Customer.objects.all()

            # Pasamos JSON
            serializer = CustomerSerializer(items, many=True)

        except Customer.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

        return Response({ "data": serializer.data }, status = status.HTTP_200_OK)

    # Insertar un cliente
    def post( self, request ):
        # Construimos el objeto apartir de lo que llega por parametro
        serializer = CustomerSerializer( data = request.data )

        # Verificamos si se pudo construir
        if serializer.is_valid():

            # Guardamos el objeto
            serializer.save()

            # Retornamos el objeto creado
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # Devolvemos los errores
            return Response({"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Actualizar una cerveza
    def put( self, request ):

        try:
            # Buscamos el objeto a actualizar
            item = Customer.objects.get(id=request.data['id'])
        except KeyError:

            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar un id"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Customer.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

        # Construimos el objeto
        serializer = CustomerSerializer( instance = item, data = request.data, partial = True )

        # Verificamos si se logro construir
        if serializer.is_valid():

            # Actualizamos la BD
            serializer.save()

            # Retornamos el objeto actualizado
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        else:
            # Devolvemos los errores
            return Response({"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Borramos una cerveza
    def delete( self, request ):

        try:
            # Buscamos el objeto a actualizar
            item = Customer.objects.get(id=request.data['id'])
            item.delete()

            # Retornamos el objeto eliminado
            return Response({"data": "Eliminado correctamente"}, status=status.HTTP_202_ACCEPTED)

        except KeyError:

            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar un id"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Customer.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

class OrderView ( APIView ):
    # Validar que primero se haya solicitado un token
    permission_classes = (IsAuthenticated, )

    def get( self, request ):

        # Verificamos si viene un ID
        try:
            # Sacamos el id de la solicitud
            id = request.data["id"]

            # Buscamos la cerveza
            items = Order.objects.get(id=id)

            # Pasamos a JSON
            serializer = OrderSerializer(items)

        except KeyError:
            # Sacamos todos las cervezas
            items = Order.objects.all()

            # Pasamos JSON
            serializer = OrderSerializer(items, many=True)

        except Order.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

        return Response({ "data": serializer.data }, status = status.HTTP_200_OK)

    # Insertar una orden
    def post( self, request ):
        # Construimos el objeto apartir de lo que llega por parametro
        serializer = OrderSerializer( data = request.data )

        # Verificamos si se pudo construir
        if serializer.is_valid():

            # Guardamos el objeto
            serializer.save()

            # Retornamos el objeto creado
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # Devolvemos los errores
            return Response({"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Actualizar una orden
    def put( self, request ):

        try:
            # Buscamos el objeto a actualizar
            item = Order.objects.get(id=request.data['id'])
        except KeyError:

            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar un id"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Order.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)

        # Construimos el objeto
        serializer = OrderSerializer( instance = item, data = request.data, partial = True )

        # Verificamos si se logro construir
        if serializer.is_valid():

            # Actualizamos la BD
            serializer.save()

            # Retornamos el objeto actualizado
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

        else:
            # Devolvemos los errores
            return Response({"errors": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Borramos una cerveza
    def delete( self, request ):

        try:
            # Buscamos el objeto a actualizar
            item = Order.objects.get(id=request.data['id'])
            item.delete()

            # Retornamos el objeto eliminado
            return Response({"data": "Eliminado correctamente"}, status=status.HTTP_202_ACCEPTED)

        except KeyError:

            # Devolvemos los errores
            return Response({"errors": "Es necesario indicar un id"}, status=status.HTTP_406_NOT_ACCEPTABLE)

        except Order.DoesNotExist:
            # Si no se ecuentra
            return Response({ "error": "No se encontro el objeto" }, status = status.HTTP_400_BAD_REQUEST)