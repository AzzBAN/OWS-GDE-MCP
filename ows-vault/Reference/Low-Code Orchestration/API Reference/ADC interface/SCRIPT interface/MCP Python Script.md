---
title: "MCP Python Script"
source: "https://1057-sg-studio.teleows.com/adc-studio-project-mgt/web/rest/help/doc/en_US/toctopics/en-us_topic_0000001357518349.html"
depth: 4
---
# MCP Python Script

Network automation allows you to define instructions using Python scripts. The following APIs are supported:

**Table 1** MCP Python Interface   
| Name | ID | Description |
| :-- | :-- | :-- |
| java.util.ArrayList | from java.util import ArrayList: java.util.ArrayList | See Open Java8 ArrayList Class API |
| java.util.HashMap | from java.util import HashMap: java.util.HashMap | See Open Java8 HashMap Class API |
| java.lang.Long | from java.lang import Long: java.lang.Long | See Open Java8 Long Class API |
| java.util.regex.Pattern | from java.util.regex import Pattern: java.util.regex.Pattern | See Open Java8 Pattern APIs |
| java.util.regex.Matcher | from java.util.regex import Matcher: java.util.regex.Matcher | See Open Java8 Matcher Class API |
| debug(self, marker, string) | from org.slf4j import Logger: debug(self, marker, string) | See Java slf4j Logger Class API |
| debug(self, marker, string, \*object) | from org.slf4j import Logger: debug(self, marker, string, \*object) | See Java slf4j Logger Class API |
| debug(self, marker, string, object) | from org.slf4j import Logger: debug(self, marker, string, object) | See Java slf4j Logger Class API |
| debug(self, marker, string, object, object1) | from org.slf4j import Logger: debug(self, marker, string, object, object1) | See Java slf4j Logger Class API |
| debug(self, marker, string, throwable) | from org.slf4j import Logger: debug(self, marker, string, throwable) | See Java slf4j Logger Class API |
| debug(self, string) | from org.slf4j import Logger: debug(self, string) | See Java slf4j Logger Class API |
| debug(self, string, \*object) | from org.slf4j import Logger: debug(self, string, \*object) | See Java slf4j Logger Class API |
| debug(self, string, object) | from org.slf4j import Logger: debug(self, string, object) | See Java slf4j Logger Class API |
| debug(self, string, object, object1) | from org.slf4j import Logger: debug(self, string, object, object1) | See Java slf4j Logger Class API |
| debug(self, string, throwable) | from org.slf4j import Logger: debug(self, string, throwable) | See Java slf4j Logger Class API |
| error(self, marker, string) | from org.slf4j import Logger: error(self, marker, string) | See Java slf4j Logger Class API |
| error(self, marker, string, \*object) | from org.slf4j import Logger: error(self, marker, string, \*object) | See Java slf4j Logger Class API |
| error(self, marker, string, object) | from org.slf4j import Logger: error(self, marker, string, object) | See Java slf4j Logger Class API |
| error(self, marker, string, object, object1) | from org.slf4j import Logger: error(self, marker, string, object, object1) | See Java slf4j Logger Class API |
| error(self, marker, string, throwable) | from org.slf4j import Logger: error(self, marker, string, throwable) | See Java slf4j Logger Class API |
| error(self, string) | from org.slf4j import Logger: error(self, string) | See Java slf4j Logger Class API |
| error(self, string, \*object) | from org.slf4j import Logger: error(self, string, \*object) | See Java slf4j Logger Class API |
| error(self, string, object) | from org.slf4j import Logger: error(self, string, object) | See Java slf4j Logger Class API |
| error(self, string, object, object1) | from org.slf4j import Logger: error(self, string, object, object1) | See Java slf4j Logger Class API |
| error(self, string, throwable) | from org.slf4j import Logger: error(self, string, throwable) | See Java slf4j Logger Class API |
| getName(self) | from org.slf4j import Logger: getName(self) | See Java slf4j Logger Class API |
| info(self, marker, string) | from org.slf4j import Logger: info(self, marker, string) | See Java slf4j Logger Class API |
| info(self, marker, string, \*object) | from org.slf4j import Logger: info(self, marker, string, \*object) | See Java slf4j Logger Class API |
| info(self, marker, string, object) | from org.slf4j import Logger: info(self, marker, string, object) | See Java slf4j Logger Class API |
| info(self, marker, string, object, object1) | from org.slf4j import Logger: info(self, marker, string, object, object1) | See Java slf4j Logger Class API |
| info(self, marker, string, throwable) | from org.slf4j import Logger: info(self, marker, string, throwable) | See Java slf4j Logger Class API |
| info(self, string) | from org.slf4j import Logger: info(self, string) | See Java slf4j Logger Class API |
| info(self, string, \*object) | from org.slf4j import Logger: info(self, string, \*object) | See Java slf4j Logger Class API |
| info(self, string, object) | from org.slf4j import Logger: info(self, string, object) | See Java slf4j Logger Class API |
| info(self, string, object, object1) | from org.slf4j import Logger: info(self, string, object, object1) | See Java slf4j Logger Class API |
| info(self, string, throwable) | from org.slf4j import Logger: info(self, string, throwable) | See Java slf4j Logger Class API |
| isDebugEnabled(self) | from org.slf4j import Logger: isDebugEnabled(self) | See Java slf4j Logger Class API |
| isDebugEnabled(self, marker) | from org.slf4j import Logger: isDebugEnabled(self, marker) | See Java slf4j Logger Class API |
| isErrorEnabled(self) | from org.slf4j import Logger: isErrorEnabled(self) | See Java slf4j Logger Class API |
| isErrorEnabled(self, marker) | from org.slf4j import Logger: isErrorEnabled(self, marker) | See Java slf4j Logger Class API |
| isInfoEnabled(self) | from org.slf4j import Logger: isInfoEnabled(self) | See Java slf4j Logger Class API |
| isInfoEnabled(self, marker) | from org.slf4j import Logger: isInfoEnabled(self, marker) | See Java slf4j Logger Class API |
| isTraceEnabled(self) | from org.slf4j import Logger: isTraceEnabled(self) | See Java slf4j Logger Class API |
| isTraceEnabled(self, marker) | from org.slf4j import Logger: isTraceEnabled(self, marker) | See Java slf4j Logger Class API |
| isWarnEnabled(self) | from org.slf4j import Logger: isWarnEnabled(self) | See Java slf4j Logger Class API |
| isWarnEnabled(self, marker) | from org.slf4j import Logger: isWarnEnabled(self, marker) | See Java slf4j Logger Class API |
| trace(self, marker, string) | from org.slf4j import Logger: trace(self, marker, string) | See Java slf4j Logger Class API |
| trace(self, marker, string, \*object) | from org.slf4j import Logger: trace(self, marker, string, \*object) | See Java slf4j Logger Class API |
| trace(self, marker, string, object) | from org.slf4j import Logger: trace(self, marker, string, object) | See Java slf4j Logger Class API |
| trace(self, marker, string, object, object1) | from org.slf4j import Logger: trace(self, marker, string, object, object1) | See Java slf4j Logger Class API |
| trace(self, marker, string, throwable) | from org.slf4j import Logger: trace(self, marker, string, throwable) | See Java slf4j Logger Class API |
| trace(self, string) | from org.slf4j import Logger: trace(self, string) | See Java slf4j Logger Class API |
| trace(self, string, \*object) | from org.slf4j import Logger: trace(self, string, \*object) | See Java slf4j Logger Class API |
| trace(self, string, object) | from org.slf4j import Logger: trace(self, string, object) | See Java slf4j Logger Class API |
| trace(self, string, object, object1) | from org.slf4j import Logger: trace(self, string, object, object1) | See Java slf4j Logger Class API |
| trace(self, string, throwable) | from org.slf4j import Logger: trace(self, string, throwable) | See Java slf4j Logger Class API |
| warn(self, marker, string) | from org.slf4j import Logger: warn(self, marker, string) | See Java slf4j Logger Class API |
| warn(self, marker, string, \*object) | from org.slf4j import Logger: warn(self, marker, string, \*object) | See Java slf4j Logger Class API |
| warn(self, marker, string, object) | from org.slf4j import Logger: warn(self, marker, string, object) | See Java slf4j Logger Class API |
| warn(self, marker, string, object, object1) | from org.slf4j import Logger: warn(self, marker, string, object, object1) | See Java slf4j Logger Class API |
| warn(self, marker, string, throwable) | from org.slf4j import Logger: warn(self, marker, string, throwable) | See Java slf4j Logger Class API |
| warn(self, string) | from org.slf4j import Logger: warn(self, string) | See Java slf4j Logger Class API |
| warn(self, string, \*object) | from org.slf4j import Logger: warn(self, string, \*object) | See Java slf4j Logger Class API |
| warn(self, string, object) | from org.slf4j import Logger: warn(self, string, object) | See Java slf4j Logger Class API |
| warn(self, string, object, object1) | from org.slf4j import Logger: warn(self, string, object, object1) | See Java slf4j Logger Class API |
| warn(self, string, throwable) | from org.slf4j import Logger: warn(self, string, throwable) | See Java slf4j Logger Class API |
| getILoggerFactory() | from org.slf4j import LoggerFactory: getILoggerFactory() | See Java slf4j LoggerFactory Class API |
| getLogger(javaClass) | from org.slf4j import LoggerFactory: getLogger(javaClass) | See Java slf4j LoggerFactory Class API |
| getLogger(string) | from org.slf4j import LoggerFactory: getLogger(string) | See Java slf4j LoggerFactory Class API |
| excluder(self) | from com.google.gson import Gson: excluder(self) | For details, see Java Gson Gson APIs. |
| fieldNamingStrategy(self) | from com.google.gson import Gson: fieldNamingStrategy(self) | For details, see Java Gson Gson APIs. |
| fromJson(self, jsonElement, javaClass) | from com.google.gson import Gson: fromJson(self, jsonElement, javaClass) | For details, see Java Gson Gson APIs. |
| fromJson(self, jsonElement, type) | from com.google.gson import Gson: fromJson(self, jsonElement, type) | For details, see Java Gson Gson APIs. |
| fromJson(self, jsonReader, type) | from com.google.gson import Gson: fromJson(self, jsonReader, type) | For details, see Java Gson Gson APIs. |
| fromJson(self, reader, javaClass) | from com.google.gson import Gson: fromJson(self, reader, javaClass) | For details, see Java Gson Gson APIs. |
| fromJson(self, reader, type) | from com.google.gson import Gson: fromJson(self, reader, type) | For details, see Java Gson Gson APIs. |
| fromJson(self, string, javaClass) | from com.google.gson import Gson: fromJson(self, string, javaClass) | For details, see Java Gson Gson APIs. |
| fromJson(self, string, type) | from com.google.gson import Gson: fromJson(self, string, type) | For details, see Java Gson Gson APIs. |
| getAdapter(self, javaClass) | from com.google.gson import Gson: getAdapter(self, javaClass) | For details, see Java Gson Gson APIs. |
| getAdapter(self, typeToken) | from com.google.gson import Gson: getAdapter(self, typeToken) | For details, see Java Gson Gson APIs. |
| getDelegateAdapter(self, typeAdapterFactory, typeToken) | from com.google.gson import Gson: getDelegateAdapter(self, typeAdapterFactory, typeToken) | For details, see Java Gson Gson APIs. |
| htmlSafe(self) | from com.google.gson import Gson: htmlSafe(self) | For details, see Java Gson Gson APIs. |
| newBuilder(self) | from com.google.gson import Gson: newBuilder(self) | For details, see Java Gson Gson APIs. |
| newJsonReader(self, reader) | from com.google.gson import Gson: newJsonReader(self, reader) | For details, see Java Gson Gson APIs. |
| newJsonWriter(self, writer) | from com.google.gson import Gson: newJsonWriter(self, writer) | For details, see Java Gson Gson APIs. |
| serializeNulls(self) | from com.google.gson import Gson: serializeNulls(self) | For details, see Java Gson Gson APIs. |
| toJson(self, jsonElement) | from com.google.gson import Gson: toJson(self, jsonElement) | For details, see Java Gson Gson APIs. |
| toJson(self, jsonElement, appendable) | from com.google.gson import Gson: toJson(self, jsonElement, appendable) | For details, see Java Gson Gson APIs. |
| toJson(self, jsonElement, jsonWriter) | from com.google.gson import Gson: toJson(self, jsonElement, jsonWriter) | For details, see Java Gson Gson APIs. |
| toJson(self, object) | from com.google.gson import Gson: toJson(self, object) | For details, see Java Gson Gson APIs. |
| toJson(self, object, appendable) | from com.google.gson import Gson: toJson(self, object, appendable) | For details, see Java Gson Gson APIs. |
| toJson(self, object, type) | from com.google.gson import Gson: toJson(self, object, type) | For details, see Java Gson Gson APIs. |
| toJson(self, object, type, appendable) | from com.google.gson import Gson: toJson(self, object, type, appendable) | For details, see Java Gson Gson APIs. |
| toJson(self, object, type, jsonWriter) | from com.google.gson import Gson: toJson(self, object, type, jsonWriter) | For details, see Java Gson Gson APIs. |
| toJsonTree(self, object) | from com.google.gson import Gson: toJsonTree(self, object) | For details, see Java Gson Gson APIs. |
| toJsonTree(self, object, type) | from com.google.gson import Gson: toJsonTree(self, object, type) | For details, see Java Gson Gson APIs. |
| parse(self, jsonReader) | from com.google.gson import JsonParser: parse(self, jsonReader) | See Java Gson JsonParser Class API |
| parse(self, reader) | from com.google.gson import JsonParser: parse(self, reader) | See Java Gson JsonParser Class API |
| parse(self, string) | from com.google.gson import JsonParser: parse(self, string) | See Java Gson JsonParser Class API |
| parseReader(jsonReader) | from com.google.gson import JsonParser: parseReader(jsonReader) | See Java Gson JsonParser Class API |
| parseReader(reader) | from com.google.gson import JsonParser: parseReader(reader) | See Java Gson JsonParser Class API |
| parseString(string) | from com.google.gson import JsonParser: parseString(string) | See Java Gson JsonParser Class API |
| add(self, string, jsonElement) | from com.google.gson import JsonObject: add(self, string, jsonElement) | See Java Gson JsonObject Class API |
| addProperty(self, string, boolean) | from com.google.gson import JsonObject: addProperty(self, string, boolean) | See Java Gson JsonObject Class API |
| addProperty(self, string, character) | from com.google.gson import JsonObject: addProperty(self, string, character) | See Java Gson JsonObject Class API |
| addProperty(self, string, number) | from com.google.gson import JsonObject: addProperty(self, string, number) | See Java Gson JsonObject Class API |
| addProperty(self, string, string1) | from com.google.gson import JsonObject: addProperty(self, string, string1) | See Java Gson JsonObject Class API |
| deepCopy(self) | from com.google.gson import JsonObject: deepCopy(self) | See Java Gson JsonObject Class API |
| entrySet(self) | from com.google.gson import JsonObject: entrySet(self) | See Java Gson JsonObject Class API |
| get(self, string) | from com.google.gson import JsonObject: get(self, string) | See Java Gson JsonObject Class API |
| getAsBigDecimal(self) | from com.google.gson import JsonObject: getAsBigDecimal(self) | See Java Gson JsonObject Class API |
| getAsBigInteger(self) | from com.google.gson import JsonObject: getAsBigInteger(self) | See Java Gson JsonObject Class API |
| getAsBoolean(self) | from com.google.gson import JsonObject: getAsBoolean(self) | See Java Gson JsonObject Class API |
| getAsByte(self) | from com.google.gson import JsonObject: getAsByte(self) | See Java Gson JsonObject Class API |
| getAsCharacter(self) | from com.google.gson import JsonObject: getAsCharacter(self) | See Java Gson JsonObject Class API |
| getAsDouble(self) | from com.google.gson import JsonObject: getAsDouble(self) | See Java Gson JsonObject Class API |
| getAsFloat(self) | from com.google.gson import JsonObject: getAsFloat(self) | See Java Gson JsonObject Class API |
| getAsInt(self) | from com.google.gson import JsonObject: getAsInt(self) | See Java Gson JsonObject Class API |
| getAsJsonArray(self) | from com.google.gson import JsonObject: getAsJsonArray(self) | See Java Gson JsonObject Class API |
| getAsJsonArray(self, string) | from com.google.gson import JsonObject: getAsJsonArray(self, string) | See Java Gson JsonObject Class API |
| getAsJsonNull(self) | from com.google.gson import JsonObject: getAsJsonNull(self) | See Java Gson JsonObject Class API |
| getAsJsonObject(self) | from com.google.gson import JsonObject: getAsJsonObject(self) | See Java Gson JsonObject Class API |
| getAsJsonObject(self, string) | from com.google.gson import JsonObject: getAsJsonObject(self, string) | See Java Gson JsonObject Class API |
| getAsJsonPrimitive(self) | from com.google.gson import JsonObject: getAsJsonPrimitive(self) | See Java Gson JsonObject Class API |
| getAsJsonPrimitive(self, string) | from com.google.gson import JsonObject: getAsJsonPrimitive(self, string) | See Java Gson JsonObject Class API |
| getAsLong(self) | from com.google.gson import JsonObject: getAsLong(self) | See Java Gson JsonObject Class API |
| getAsNumber(self) | from com.google.gson import JsonObject: getAsNumber(self) | See Java Gson JsonObject Class API |
| getAsShort(self) | from com.google.gson import JsonObject: getAsShort(self) | See Java Gson JsonObject Class API |
| getAsString(self) | from com.google.gson import JsonObject: getAsString(self) | See Java Gson JsonObject Class API |
| has(self, string) | from com.google.gson import JsonObject: has(self, string) | See Java Gson JsonObject Class API |
| isJsonArray(self) | from com.google.gson import JsonObject: isJsonArray(self) | See Java Gson JsonObject Class API |
| isJsonNull(self) | from com.google.gson import JsonObject: isJsonNull(self) | See Java Gson JsonObject Class API |
| isJsonObject(self) | from com.google.gson import JsonObject: isJsonObject(self) | See Java Gson JsonObject Class API |
| isJsonPrimitive(self) | from com.google.gson import JsonObject: isJsonPrimitive(self) | See Java Gson JsonObject Class API |
| keySet(self) | from com.google.gson import JsonObject: keySet(self) | See Java Gson JsonObject Class API |
| remove(self, string) | from com.google.gson import JsonObject: remove(self, string) | See Java Gson JsonObject Class API |
| size(self) | from com.google.gson import JsonObject: size(self) | See Java Gson JsonObject Class API |
| add(self, boolean) | from com.google.gson import JsonArray: add(self, boolean) | For details, see Java Gson JsonArray APIs. |
| add(self, character) | from com.google.gson import JsonArray: add(self, character) | For details, see Java Gson JsonArray APIs. |
| add(self, jsonElement) | from com.google.gson import JsonArray: add(self, jsonElement) | For details, see Java Gson JsonArray APIs. |
| add(self, number) | from com.google.gson import JsonArray: add(self, number) | For details, see Java Gson JsonArray APIs. |
| add(self, string) | from com.google.gson import JsonArray: add(self, string) | For details, see Java Gson JsonArray APIs. |
| addAll(self, jsonArray) | from com.google.gson import JsonArray: addAll(self, jsonArray) | For details, see Java Gson JsonArray APIs. |
| contains(self, jsonElement) | from com.google.gson import JsonArray: contains(self, jsonElement) | For details, see Java Gson JsonArray APIs. |
| deepCopy(self) | from com.google.gson import JsonArray: deepCopy(self) | For details, see Java Gson JsonArray APIs. |
| get(self, int) | from com.google.gson import JsonArray: get(self, int) | For details, see Java Gson JsonArray APIs. |
| getAsBigDecimal(self) | from com.google.gson import JsonArray: getAsBigDecimal(self) | For details, see Java Gson JsonArray APIs. |
| getAsBigInteger(self) | from com.google.gson import JsonArray: getAsBigInteger(self) | For details, see Java Gson JsonArray APIs. |
| getAsBoolean(self) | from com.google.gson import JsonArray: getAsBoolean(self) | For details, see Java Gson JsonArray APIs. |
| getAsByte(self) | from com.google.gson import JsonArray: getAsByte(self) | For details, see Java Gson JsonArray APIs. |
| getAsCharacter(self) | from com.google.gson import JsonArray: getAsCharacter(self) | For details, see Java Gson JsonArray APIs. |
| getAsDouble(self) | from com.google.gson import JsonArray: getAsDouble(self) | For details, see Java Gson JsonArray APIs. |
| getAsFloat(self) | from com.google.gson import JsonArray: getAsFloat(self) | For details, see Java Gson JsonArray APIs. |
| getAsInt(self) | from com.google.gson import JsonArray: getAsInt(self) | For details, see Java Gson JsonArray APIs. |
| getAsJsonArray(self) | from com.google.gson import JsonArray: getAsJsonArray(self) | For details, see Java Gson JsonArray APIs. |
| getAsJsonNull(self) | from com.google.gson import JsonArray: getAsJsonNull(self) | For details, see Java Gson JsonArray APIs. |
| getAsJsonObject(self) | from com.google.gson import JsonArray: getAsJsonObject(self) | For details, see Java Gson JsonArray APIs. |
| getAsJsonPrimitive(self) | from com.google.gson import JsonArray: getAsJsonPrimitive(self) | For details, see Java Gson JsonArray APIs. |
| getAsLong(self) | from com.google.gson import JsonArray: getAsLong(self) | For details, see Java Gson JsonArray APIs. |
| getAsNumber(self) | from com.google.gson import JsonArray: getAsNumber(self) | For details, see Java Gson JsonArray APIs. |
| getAsShort(self) | from com.google.gson import JsonArray: getAsShort(self) | For details, see Java Gson JsonArray APIs. |
| getAsString(self) | from com.google.gson import JsonArray: getAsString(self) | For details, see Java Gson JsonArray APIs. |
| isEmpty(self) | from com.google.gson import JsonArray: isEmpty(self) | For details, see Java Gson JsonArray APIs. |
| isJsonArray(self) | from com.google.gson import JsonArray: isJsonArray(self) | For details, see Java Gson JsonArray APIs. |
| isJsonNull(self) | from com.google.gson import JsonArray: isJsonNull(self) | For details, see Java Gson JsonArray APIs. |
| isJsonObject(self) | from com.google.gson import JsonArray: isJsonObject(self) | For details, see Java Gson JsonArray APIs. |
| isJsonPrimitive(self) | from com.google.gson import JsonArray: isJsonPrimitive(self) | For details, see Java Gson JsonArray APIs. |
| remove(self, int) | from com.google.gson import JsonArray: remove(self, int) | For details, see Java Gson JsonArray APIs. |
| remove(self, jsonElement) | from com.google.gson import JsonArray: remove(self, jsonElement) | For details, see Java Gson JsonArray APIs. |
| set(self, int, jsonElement) | from com.google.gson import JsonArray: set(self, int, jsonElement) | For details, see Java Gson JsonArray APIs. |
| size(self) | from com.google.gson import JsonArray: size(self) | For details, see Java Gson JsonArray APIs. |
| deepCopy(self) | from com.google.gson import JsonNull: deepCopy(self) | See Java Gson JsonNull Class API |
| getAsBigDecimal(self) | from com.google.gson import JsonNull: getAsBigDecimal(self) | See Java Gson JsonNull Class API |
| getAsBigInteger(self) | from com.google.gson import JsonNull: getAsBigInteger(self) | See Java Gson JsonNull Class API |
| getAsBoolean(self) | from com.google.gson import JsonNull: getAsBoolean(self) | See Java Gson JsonNull Class API |
| getAsByte(self) | from com.google.gson import JsonNull: getAsByte(self) | See Java Gson JsonNull Class API |
| getAsCharacter(self) | from com.google.gson import JsonNull: getAsCharacter(self) | See Java Gson JsonNull Class API |
| getAsDouble(self) | from com.google.gson import JsonNull: getAsDouble(self) | See Java Gson JsonNull Class API |
| getAsFloat(self) | from com.google.gson import JsonNull: getAsFloat(self) | See Java Gson JsonNull Class API |
| getAsInt(self) | from com.google.gson import JsonNull: getAsInt(self) | See Java Gson JsonNull Class API |
| getAsJsonArray(self) | from com.google.gson import JsonNull: getAsJsonArray(self) | See Java Gson JsonNull Class API |
| getAsJsonNull(self) | from com.google.gson import JsonNull: getAsJsonNull(self) | See Java Gson JsonNull Class API |
| getAsJsonObject(self) | from com.google.gson import JsonNull: getAsJsonObject(self) | See Java Gson JsonNull Class API |
| getAsJsonPrimitive(self) | from com.google.gson import JsonNull: getAsJsonPrimitive(self) | See Java Gson JsonNull Class API |
| getAsLong(self) | from com.google.gson import JsonNull: getAsLong(self) | See Java Gson JsonNull Class API |
| getAsNumber(self) | from com.google.gson import JsonNull: getAsNumber(self) | See Java Gson JsonNull Class API |
| getAsShort(self) | from com.google.gson import JsonNull: getAsShort(self) | See Java Gson JsonNull Class API |
| getAsString(self) | from com.google.gson import JsonNull: getAsString(self) | See Java Gson JsonNull Class API |
| isJsonArray(self) | from com.google.gson import JsonNull: isJsonArray(self) | See Java Gson JsonNull Class API |
| isJsonNull(self) | from com.google.gson import JsonNull: isJsonNull(self) | See Java Gson JsonNull Class API |
| isJsonObject(self) | from com.google.gson import JsonNull: isJsonObject(self) | See Java Gson JsonNull Class API |
| isJsonPrimitive(self) | from com.google.gson import JsonNull: isJsonPrimitive(self) | See Java Gson JsonNull Class API |
| asctime() | import time: asctime() | For details, see the Python time library. |
| asctime(object) | import time: asctime(object) | For details, see the Python time library. |
| classDictInit(object) | import time: classDictInit(object) | For details, see the Python time library. |
| clock() | import time: clock() | For details, see the Python time library. |
| ctime() | import time: ctime() | For details, see the Python time library. |
| ctime(object) | import time: ctime(object) | For details, see the Python time library. |
| gmtime() | import time: gmtime() | For details, see the Python time library. |
| gmtime(object) | import time: gmtime(object) | For details, see the Python time library. |
| locale\_asctime(tuple) | import time: locale\_asctime(tuple) | For details, see the Python time library. |
| localtime() | import time: localtime() | For details, see the Python time library. |
| localtime(object) | import time: localtime(object) | For details, see the Python time library. |
| mktime(tuple) | import time: mktime(tuple) | For details, see the Python time library. |
| parseTimeDoubleArg(object) | import time: parseTimeDoubleArg(object) | For details, see the Python time library. |
| sleep(double) | import time: sleep(double) | For details, see the Python time library. |
| strftime(string) | import time: strftime(string) | For details, see the Python time library. |
| strftime(string, tuple) | import time: strftime(string, tuple) | For details, see the Python time library. |
| strptime(string) | import time: strptime(string) | For details, see the Python time library. |
| strptime(string, string1) | import time: strptime(string, string1) | For details, see the Python time library. |
| time() | import time: time() | For details, see the Python time library. |
| close(self) | from StringIO import StringIO: close(self) | For details, see StringIO APIs in the Python StringIO library. |
| flush(self) | from StringIO import StringIO: flush(self) | For details, see StringIO APIs in the Python StringIO library. |
| getvalue(self) | from StringIO import StringIO: getvalue(self) | For details, see StringIO APIs in the Python StringIO library. |
| isatty(self) | from StringIO import StringIO: isatty(self) | For details, see StringIO APIs in the Python StringIO library. |
| next(self) | from StringIO import StringIO: next(self) | For details, see StringIO APIs in the Python StringIO library. |
| read(self, n=1) | from StringIO import StringIO: read(self, n=1) | For details, see StringIO APIs in the Python StringIO library. |
| readline(self, length=None) | from StringIO import StringIO: readline(self, length=None) | For details, see StringIO APIs in the Python StringIO library. |
| readlines(self, sizehint=0) | from StringIO import StringIO: readlines(self, sizehint=0) | For details, see StringIO APIs in the Python StringIO library. |
| seek(self, pos, mode=0) | from StringIO import StringIO: seek(self, pos, mode=0) | For details, see StringIO APIs in the Python StringIO library. |
| tell(self) | from StringIO import StringIO: tell(self) | For details, see StringIO APIs in the Python StringIO library. |
| truncate(self, size=None) | from StringIO import StringIO: truncate(self, size=None) | For details, see StringIO APIs in the Python StringIO library. |
| write(self, s) | from StringIO import StringIO: write(self, s) | For details, see StringIO APIs in the Python StringIO library. |
| writelines(self, iterable) | from StringIO import StringIO: writelines(self, iterable) | For details, see StringIO APIs in the Python StringIO library. |
| compile(pattern, flags=0) | import re: compile(pattern, flags=0) | See the python re library. |
| escape(pattern) | import re: escape(pattern) | See the python re library. |
| findall(pattern, string, flags=0) | import re: findall(pattern, string, flags=0) | See the python re library. |
| match(pattern, string, flags=0) | import re: match(pattern, string, flags=0) | See the python re library. |
| purge() | import re: purge() | See the python re library. |
| search(pattern, string, flags=0) | import re: search(pattern, string, flags=0) | See the python re library. |
| split(pattern, string, maxsplit=0, flags=0) | import re: split(pattern, string, maxsplit=0, flags=0) | See the python re library. |
| sub(pattern, repl, string, count=0, flags=0) | import re: sub(pattern, repl, string, count=0, flags=0) | See the python re library. |
| subn(pattern, repl, string, count=0, flags=0) | import re: subn(pattern, repl, string, count=0, flags=0) | See the python re library. |
| template(pattern, flags=0) | import re: template(pattern, flags=0) | See the python re library. |
| days(self) | from datetime import timedelta: days(self) | For details, see the timedelta API in the python datetime library. |
| microseconds(self) | from datetime import timedelta: microseconds(self) | For details, see the timedelta API in the python datetime library. |
| seconds(self) | from datetime import timedelta: seconds(self) | For details, see the timedelta API in the python datetime library. |
| total\_seconds(self) | from datetime import timedelta: total\_seconds(self) | For details, see the timedelta API in the python datetime library. |
| ctime(self) | from datetime import date: ctime(self) | For details, see the date type API in the python datetime library. |
| day(self) | from datetime import date: day(self) | For details, see the date type API in the python datetime library. |
| fromordinal(cls, n) | from datetime import date: fromordinal(cls, n) | For details, see the date type API in the python datetime library. |
| fromtimestamp(cls, t) | from datetime import date: fromtimestamp(cls, t) | For details, see the date type API in the python datetime library. |
| isocalendar(self) | from datetime import date: isocalendar(self) | For details, see the date type API in the python datetime library. |
| isoformat(self) | from datetime import date: isoformat(self) | For details, see the date type API in the python datetime library. |
| isoweekday(self) | from datetime import date: isoweekday(self) | For details, see the date type API in the python datetime library. |
| month(self) | from datetime import date: month(self) | For details, see the date type API in the python datetime library. |
| replace(self, year=None, month=None, day=None) | from datetime import date: replace(self, year=None, month=None, day=None) | For details, see the date type API in the python datetime library. |
| strftime(self, fmt) | from datetime import date: strftime(self, fmt) | For details, see the date type API in the python datetime library. |
| timetuple(self) | from datetime import date: timetuple(self) | For details, see the date type API in the python datetime library. |
| today(cls) | from datetime import date: today(cls) | For details, see the date type API in the python datetime library. |
| toordinal(self) | from datetime import date: toordinal(self) | For details, see the date type API in the python datetime library. |
| weekday(self) | from datetime import date: weekday(self) | For details, see the date type API in the python datetime library. |
| year(self) | from datetime import date: year(self) | For details, see the date type API in the python datetime library. |
| dst(self, dt) | from datetime import tzinfo: dst(self, dt) | For details, see the tzinfo API in the python datetime library. |
| fromutc(self, dt) | from datetime import tzinfo: fromutc(self, dt) | For details, see the tzinfo API in the python datetime library. |
| tzname(self, dt) | from datetime import tzinfo: tzname(self, dt) | For details, see the tzinfo API in the python datetime library. |
| utcoffset(self, dt) | from datetime import tzinfo: utcoffset(self, dt) | For details, see the tzinfo API in the python datetime library. |
| dst(self) | from datetime import time: dst(self) | For details, see the time type API in the python datetime library. |
| hour(self) | from datetime import time: hour(self) | For details, see the time type API in the python datetime library. |
| isoformat(self) | from datetime import time: isoformat(self) | For details, see the time type API in the python datetime library. |
| microsecond(self) | from datetime import time: microsecond(self) | For details, see the time type API in the python datetime library. |
| minute(self) | from datetime import time: minute(self) | For details, see the time type API in the python datetime library. |
| replace(self, hour=None, minute=None, second=None, microsecond=None, tzinfo=True) | from datetime import time: replace(self, hour=None, minute=None, second=None, microsecond=None, tzinfo=True) | For details, see the time type API in the python datetime library. |
| second(self) | from datetime import time: second(self) | For details, see the time type API in the python datetime library. |
| strftime(self, fmt) | from datetime import time: strftime(self, fmt) | For details, see the time type API in the python datetime library. |
| tzinfo(self) | from datetime import time: tzinfo(self) | For details, see the time type API in the python datetime library. |
| tzname(self) | from datetime import time: tzname(self) | For details, see the time type API in the python datetime library. |
| utcoffset(self) | from datetime import time: utcoffset(self) | For details, see the time type API in the python datetime library. |
| astimezone(self, tz) | from datetime import datetime: astimezone(self, tz) | For details, see the datetime type API in the python datetime library. |
| combine(cls, date, time) | from datetime import datetime: combine(cls, date, time) | For details, see the datetime type API in the python datetime library. |
| ctime(self) | from datetime import datetime: ctime(self) | For details, see the datetime type API in the python datetime library. |
| date(self) | from datetime import datetime: date(self) | For details, see the datetime type API in the python datetime library. |
| dst(self) | from datetime import datetime: dst(self) | For details, see the datetime type API in the python datetime library. |
| fromtimestamp(cls, t, tz=None) | from datetime import datetime: fromtimestamp(cls, t, tz=None) | For details, see the datetime type API in the python datetime library. |
| hour(self) | from datetime import datetime: hour(self) | For details, see the datetime type API in the python datetime library. |
| isoformat(self, sep='T') | from datetime import datetime: isoformat(self, sep='T') | For details, see the datetime type API in the python datetime library. |
| microsecond(self) | from datetime import datetime: microsecond(self) | For details, see the datetime type API in the python datetime library. |
| minute(self) | from datetime import datetime: minute(self) | For details, see the datetime type API in the python datetime library. |
| now(cls, tz=None) | from datetime import datetime: now(cls, tz=None) | For details, see the datetime type API in the python datetime library. |
| replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=True) | from datetime import datetime: replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=True) | For details, see the datetime type API in the python datetime library. |
| second(self) | from datetime import datetime: second(self) | For details, see the datetime type API in the python datetime library. |
| strptime(cls, date\_string, format) | from datetime import datetime: strptime(cls, date\_string, format) | For details, see the datetime type API in the python datetime library. |
| time(self) | from datetime import datetime: time(self) | For details, see the datetime type API in the python datetime library. |
| timetuple(self) | from datetime import datetime: timetuple(self) | For details, see the datetime type API in the python datetime library. |
| timetz(self) | from datetime import datetime: timetz(self) | For details, see the datetime type API in the python datetime library. |
| tzinfo(self) | from datetime import datetime: tzinfo(self) | For details, see the datetime type API in the python datetime library. |
| tzname(self) | from datetime import datetime: tzname(self) | For details, see the datetime type API in the python datetime library. |
| utcfromtimestamp(cls, t) | from datetime import datetime: utcfromtimestamp(cls, t) | For details, see the datetime type API in the python datetime library. |
| utcnow(cls) | from datetime import datetime: utcnow(cls) | For details, see the datetime type API in the python datetime library. |
| utcoffset(self) | from datetime import datetime: utcoffset(self) | For details, see the datetime type API in the python datetime library. |
| utctimetuple(self) | from datetime import datetime: utctimetuple(self) | For details, see the datetime type API in the python datetime library. |
| dump(obj, fp, skipkeys=False, ensure\_ascii=True, check\_circular=True, allow\_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort\_keys=False) | import json: dump(obj, fp, skipkeys=False, ensure\_ascii=True, check\_circular=True, allow\_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort\_keys=False) | For details, see the Python JSON library. |
| dumps(obj, skipkeys=False, ensure\_ascii=True, check\_circular=True, allow\_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort\_keys=False) | import json: dumps(obj, skipkeys=False, ensure\_ascii=True, check\_circular=True, allow\_nan=True, cls=None, indent=None, separators=None, encoding='utf-8', default=None, sort\_keys=False) | For details, see the Python JSON library. |
| load(fp, encoding=None, cls=None, object\_hook=None, parse\_float=None, parse\_int=None, parse\_constant=None, object\_pairs\_hook=None) | import json: load(fp, encoding=None, cls=None, object\_hook=None, parse\_float=None, parse\_int=None, parse\_constant=None, object\_pairs\_hook=None) | For details, see the Python JSON library. |
| loads(s, encoding=None, cls=None, object\_hook=None, parse\_float=None, parse\_int=None, parse\_constant=None, object\_pairs\_hook=None) | import json: loads(s, encoding=None, cls=None, object\_hook=None, parse\_float=None, parse\_int=None, parse\_constant=None, object\_pairs\_hook=None) | For details, see the Python JSON library. |
| convertHash2JsonStr(self, result) | Command\_Executor\_Base: convertHash2JsonStr(self, result) | Command execution base script API: converts hash objects into JSON character strings. |
| convertHash2JsonStr(self, result) | Result\_Analyzer\_Base: convertHash2JsonStr(self, result) | Result analysis base script API: converts hash objects into JSON character strings. |
| sendCommand(self, channel, params, commandInfo, originalCmd) | Other\_To\_Rest\_Command\_Executor\_Base: sendCommand(self, channel, params, commandInfo, originalCmd) | Base script API customized for the REST protocol: null |
| getPassword(self) | com.huawei.mcp.connect.CommandChannelScript: getPassword(self) | Command Delivery API |
| getUsername(self) | com.huawei.mcp.connect.CommandChannelScript: getUsername(self) | Command Delivery API |
| sendForRest(self, header, uriVariables, params, body, waitResultTime) | com.huawei.mcp.connect.CommandChannelScript: sendForRest(self, header, uriVariables, params, body, waitResultTime) | Command Delivery API |
| sendForRest(self, method, url, header, uriVariables, params, body, waitResultTime) | com.huawei.mcp.connect.CommandChannelScript: sendForRest(self, method, url, header, uriVariables, params, body, waitResultTime) | Command Delivery API |
| sendForRuby(self, markPara, cmd, end, waitResultTime) | com.huawei.mcp.connect.CommandChannelScript: sendForRuby(self, markPara, cmd, end, waitResultTime) | Command Delivery API |
| sendForRuby(self, markPara, cmd, end, waitResultTime, timeOut) | com.huawei.mcp.connect.CommandChannelScript: sendForRuby(self, markPara, cmd, end, waitResultTime, timeOut) | Command Delivery API |
| waitForCallbackService(self, key, timeoutInMills) | com.huawei.mcp.connect.CommandChannelScript: waitForCallbackService(self, key, timeoutInMills) | Command Delivery API |
| sendCommand(self, channel, param, commandInfo, originalCmd) | com.huawei.mcp.script.intf.OtherToResultCommandExecutor: sendCommand(self, channel, param, commandInfo, originalCmd) | When a command is sent to the peer device, the original protocol command content is used as the input parameter. This script is invoked to invoke the channel.sendForRest interface in the script to send REST commands. Application scenario: Currently, there are a large number of command assets and upper-layer assets of other protocol types. You do not want to change the upper-layer logic. Instead, you only want to use the REST protocol to send commands and interconnect with the REST system on the premise that inventory assets are compatible. | **Parent topic:** [[SCRIPT interface|SCRIPT interface]]