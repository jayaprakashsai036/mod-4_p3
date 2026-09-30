package com.example.mod4_p3

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

data class ApiRequest(
    val session_id: String,
    val message: String
)

data class ApiResponse(
    val reply: String,
    val history_length: Int
)

data class HealthResponse(
    val status: String
)

interface ApiService {
    @POST("chat")
    suspend fun sendMessage(@Body request: ApiRequest): ApiResponse

    @GET("health")
    suspend fun health(): HealthResponse
}

object RetrofitClient {
    private const val BASE_URL = "http://10.0.2.2:8000/"

    val apiService: ApiService by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
            .create(ApiService::class.java)
    }
}
